from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from registration.forms import RegistrationFrom


def registration(request: HttpRequest) -> HttpResponse:
    print(request.method)
    if request.method == 'GET':
        form = RegistrationFrom()
        template = r'registration\index.html'
        return render(request, template, {'form': form})
