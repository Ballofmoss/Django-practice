from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.http import HttpRequest
from django.contrib.auth.models import User
from account.models.profile import Profile
from django.contrib.auth.decorators import login_required
from account.forms import UpdateUserForm, UpdateProfileForm
# kot
# 5yxpPQ0rz_
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
    
@login_required(login_url='login')
def profile_view(request: HttpRequest):
    user = Profile.objects.select_related('user').get(user=request.user)
    return render(request, 'profile.html', context={
        'user' : user
    })
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        print(user_form.errors.as_text())
        print(profile_form.errors.as_text())
        if user_form.is_valid() and profile_form.is_valid():
         
            user_form_result =  user_form.save()
            profile_form_result = profile_form.save()
            user_form_result.save()
            profile_form_result.save()
        return redirect('/user/profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        return render(request, 'change_profile.html', {'user_form': user_form, 'profile_form': profile_form})

