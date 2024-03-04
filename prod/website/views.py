from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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

def customer_record(request, pk):
    if request.user.is_authenticated:
        personal_data = Record.objects.get(id=pk)
        return render(request, 'record.html', {'personal_data':personal_data})
    else:
        messages.success(request, 'Вы должны войти в систему прежде чем войти сюда!')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        personal_data = Record.objects.get(id=pk)
        personal_data.delete()
        messages.success(request, 'Пользователь успешно удален!')
        return redirect('home')
    else:
        messages.success(request, 'Вы должны войти в систему прежде чем сделать сюда!')
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Пользователь успешно добавлен!')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, 'Вы должны войти в систему прежде чем сделать сюда!')
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_data = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены!')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, 'Вы должны войти в систему прежде чем сделать сюда!')
        return redirect('home')