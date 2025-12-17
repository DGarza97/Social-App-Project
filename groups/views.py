from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Group

@login_required
def groups_page(request):
    if request.method == "POST":
        Group.objects.create(
            name=request.POST["name"],
            description=request.POST["description"],
            owner=request.user
        )
        return redirect("groups")

    groups = Group.objects.all()
    return render(request, "groups/groups.html", {
        "groups": groups
    })


@login_required
def join_group(request, group_id):
    group = Group.objects.create(
        name=request.POST["name"],
        description=request.POST["description"],
        owner=request.user
    )
    group.members.add(request.user)
    return redirect("groups")
