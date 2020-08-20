from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
        return redirect('accounts/signup')
    else:
        form = UserCreationForm()  # 비어있는 회원가입 폼을 생성한다.
        return render(request, 'accounts/form.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect('posts:index')
        return redirect('accounts:login')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/form.html', {'form': form})


def logout(request):
    user_logout(request)
    return redirect('posts:index')
