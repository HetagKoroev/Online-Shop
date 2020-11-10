from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from registration.forms import RegistrationFrom


def registration(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = RegistrationFrom()
        template = r'registration\index.html'
        return render(request, template, {'form': form})
    if request.method == 'POST':
        for x in request.POST.items():
            print(x)
        return redirect('home')
