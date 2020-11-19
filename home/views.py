from typing import Union
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Platform, Category, ConcreteService
from services.logic import get_all_objects_from_model
from django.contrib.auth.models import User


def home(request: HttpRequest) -> Union[HttpResponse, None]:
    if request.method == 'GET':
        platforms = get_all_objects_from_model(Platform)
        categories = get_all_objects_from_model(Category)
        concrete_services = get_all_objects_from_model(ConcreteService)

        context = {'platforms': platforms,
                   'categories': categories,
                   'concrete_services': concrete_services
                   }

        template = r'home\index.html'
        return render(request, template_name=template, context=context)
