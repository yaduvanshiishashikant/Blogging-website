from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passward = request.POST.get('password')
        User.objects.create_user(
            username = username,
            password = passward
        )
        return redirect('login')
    return render(request, 'accounts/register.html')

def user_logout(request):
    logout(request)
    return redirect('home')