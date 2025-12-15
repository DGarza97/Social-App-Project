from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

@login_required
def feed_page(request):
    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Post.objects.create(
                author=request.user,
                content=request.POST['content']
            )

    posts = Post.objects.order_by("-created_at")

    return render(request, "feed/feed.html", {
        "posts": posts
    })


