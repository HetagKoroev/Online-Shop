from typing import Union
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Platform, Category, ConcreteService
from django.contrib.auth.decorators import login_required


# @login_required
def home(request: HttpRequest) -> Union[HttpResponse, None]:
    if request.method == 'GET':
        platforms = Platform.objects.all()
        categories = Category.objects.all()
        concrete_services = ConcreteService.objects.all()

        context = {
                   'platforms': platforms,
                   'categories': categories,
                   'concrete_services': concrete_services
                   }

        template = r'home\index.html'
        return render(request, template_name=template, context=context)
