from django.shortcuts import render, redirect, get_object_or_404
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

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed') 
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/editpost.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        return redirect('feed')

    return render(request, 'posts/deletepost.html', {'post': post})



