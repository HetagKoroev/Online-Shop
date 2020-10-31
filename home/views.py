from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Service, Category, ConcreteProduct
from services.logic import _get_all_model_objects


def home(request: HttpRequest) -> HttpResponse:
    services = _get_all_model_objects(Service)
    categories = _get_all_model_objects(Category)
    concrete_products = _get_all_model_objects(ConcreteProduct)

    context = {'concrete_products': concrete_products,
               'services': services,
               'categories': categories}

    template = r'home\index.html'
    return render(request, template_name=template, context=context)
