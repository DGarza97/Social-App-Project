from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import PostForm
from .models import Post


@login_required
def feed_page(request):
    if request.method == "POST":
        content = request.POST.get("content")

        if content:
            Post.objects.create(
                author=request.user,
                content=content
            )

    posts = Post.objects.order_by("-created_at")

    return render(request, "feed/feed.html", {
        "posts": posts
    })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            next_url = request.POST.get("next")
            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}
            ):
                return redirect(next_url)

            return redirect("feed")
    else:
        form = PostForm(instance=post)

    return render(request, "posts/editpost.html", {
        "form": form,
        "next": request.GET.get("next", request.META.get("HTTP_REFERER", "/")),
    })


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()

        next_url = request.POST.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url, allowed_hosts={request.get_host()}
        ):
            return redirect(next_url)

        return redirect("feed")

    return render(request, "posts/deletepost.html", {
        "post": post,
        "next": request.GET.get("next", request.META.get("HTTP_REFERER", "/")),
    })



