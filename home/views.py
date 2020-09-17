from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Service, Category, ConcreteProduct
from .services.logic import get_all_model_objects


def home(request: HttpRequest) -> HttpResponse:
    services = get_all_model_objects(Service)
    categories = get_all_model_objects(Category)
    concrete_products = get_all_model_objects(ConcreteProduct)

    context = {'concrete_products': concrete_products,
               'services': services,
               'categories': categories}
    template = 'index.html'
    return render(request, template_name=template, context=context)
