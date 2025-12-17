from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio"]
        widgets = {"bio": forms.Textarea(attrs={"rows": 4})}

@login_required
def my_profile(request):
    profile = request.user.profile
    return render(request, "profile/profile.html", {"profile": profile})

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")  # back to your profile page
    else:
        form = ProfileForm(instance=profile)

    return render(request, "profile/edit_profile.html", {"form": form})
