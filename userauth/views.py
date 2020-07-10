from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import RegistrationForm, LoginForm, EditProfileForm, ChangePasswordForm


def home(request):
    context = {'user': request.user}
    return render(request, 'userauth/home.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    context = {}
    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username, password = form.cleaned_data.get(
                'username'), form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                messages.success(request, f'Welcome back {username}!')
                return redirect('home')
            else:
                messages.error(request,
                               f'Your account seems to be inactive...')
                context['form'] = form
        else:
            messages.error(request, f'Please check your Login details...')
            context['form'] = form
    else:
        form = LoginForm()
        context['form'] = form
    return render(request, 'userauth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Welcome to Auth App!'))
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'userauth/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Changes saved!'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'userauth/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('Password saved!'))
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
    context = {'form': form}
    return render(request, 'userauth/change_password.html', context)