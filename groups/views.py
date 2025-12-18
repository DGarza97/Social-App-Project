from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Group


@login_required
def groups_page(request):
    # CREATE GROUP
    if request.method == "POST":
        Group.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            owner=request.user
        )
        return redirect("groups")

    # LIST GROUPS
    groups = Group.objects.all()
    return render(request, "groups/groups.html", {
        "groups": groups
    })


@login_required
def join_group(request, group_id):
    if request.method == "POST":
        group = get_object_or_404(Group, id=group_id)
        group.members.add(request.user)

    return redirect("groups")
