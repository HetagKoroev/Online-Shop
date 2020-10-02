from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def registration(request: HttpRequest) -> HttpResponse:
    template = r'registration\index.html'
    return render(request, template_name=template)
