from typing import Union, Type
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Platform, Category, ConcreteService
from services.logic import get_all_objects_from_model
from django.contrib.auth.decorators import login_required


# @login_required
def home(request: HttpRequest) -> Union[HttpResponse, None]:
    if request.method == 'GET':
        platforms = get_all_objects_from_model(Type[Platform])
        categories = get_all_objects_from_model(Type[Category])
        concrete_services = get_all_objects_from_model(Type[ConcreteService])

        context = {'platforms': platforms,
                   'categories': categories,
                   'concrete_services': concrete_services
                   }

        template = r'home\index.html'
        return render(request, template_name=template, context=context)
