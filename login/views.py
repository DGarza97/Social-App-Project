from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_page(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate against the auth_user table
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            error = "Invalid username or password."

    return render(request, 'login/login.html', {'error': error})
