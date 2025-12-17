from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from feed.models import Post

@login_required
def my_projects(request):
    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Post.objects.create(
                author=request.user,
                content=content
            )
            return redirect(request.path)

    posts = Post.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "myprojects/myprojects.html", {
        "posts": posts
    })
