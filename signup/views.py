from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        #password validation
        if password1 != password2:
            return render(request, "signup/signup.html", {
                "error": "Passwords do not match"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "signup/signup.html", {
                "error": "Username already exists"
            })

        if User.objects.filter(email=email).exists():
            return render(request, "signup/signup.html", {
                "error": "Email already registered"
            })

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect("login")

    return render(request, "signup/signup.html")
