from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.http import HttpRequest
from django.contrib.auth.models import User

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


