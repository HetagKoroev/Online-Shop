from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Домашняя страница</h1>')


class Home(View):
    pass
