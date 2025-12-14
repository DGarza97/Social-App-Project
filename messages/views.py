from django.shortcuts import render

def messages_page(request):
    return render(request, "messages/messages.html")

# def feed_page(request):
#     return render(request, 'feed/feed.html')

# def myprojects(request):
#     return render(request, 'myprojects/myprojects.html')
