from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feed.models import Post

def my_projects(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'myprojects/myprojects.html', {'posts': posts})
