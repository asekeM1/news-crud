from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Успешно! Вы успешно авторизовались!')
            return redirect('home')
        else:
            messages.success(request, 'Упс! Что-то пошло не так..')
            return redirect('home')
    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из профиля')
    return redirect('home')

