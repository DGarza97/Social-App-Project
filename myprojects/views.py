from django.shortcuts import render

def feed_page(request):
    return render(request, 'feed/feed.html')

def myprojects(request):
    return render(request, 'myprojects/myprojects.html')