from typing import Union
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Service, Category, ConcreteProduct
from services.logic import get_all_objects_from_model


def home(request: HttpRequest) -> Union[HttpResponse, None]:
    print(request.path)
    if request.method == 'GET':
        services = get_all_objects_from_model(Service)
        categories = get_all_objects_from_model(Category)
        concrete_products = get_all_objects_from_model(ConcreteProduct)

        context = {'concrete_products': concrete_products,
                   'services': services,
                   'categories': categories}

        template = r'home\index.html'
        return render(request, template_name=template, context=context)
