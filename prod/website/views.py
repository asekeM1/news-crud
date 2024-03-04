from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
def home(request):
    records = Record.objects.all()

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
    return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из профиля')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

