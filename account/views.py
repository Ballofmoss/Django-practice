from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.http import HttpRequest
from django.contrib.auth.models import User

# jaba
# -BeM8GueMJ
def register(request:HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.errors.as_text())
        if form.is_valid():

            user = form.save()
            user.save()
            return redirect('home')
        return redirect('register')
    else:
        form = RegisterForm()
        return render(request, 'register.html', context={
            'title': 'Регистрация',
            'form': form,
        })
        
def login_user(request:HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else: 
        form = LoginForm()
    return render(request, 'login.html', context={
        'title': 'Авторизация',
        'form': form,
    })
def logout_user(request:HttpRequest):
        logout(request)
        return redirect('home')


