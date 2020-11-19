from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User


def registration(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            return render(request, 'registration/index.html', {'form': form})

    elif request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'registration/index.html', {'form': form})
