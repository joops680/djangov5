from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    print(user)
    if user is None:
        return HttpResponseRedirect(
        reverse('user_auth:login_user')
        )
    else:
        login(request, user)
        return render(request, 'home.html', 
    {
    "username": request.user.username,
    "password": request.user.password}
    )
    

#def user_register(request):
    #return render(request, 'register.html')

def home(request):
    return render(request, 'return_home.html', 
    {
    "username": request.user.username,
    "password": request.user.password}
    )