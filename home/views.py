from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Service, Category, ConcreteProduct
from .services.logic import get_all_model_objects


def home(request):
    allob = get_all_model_objects(ConcreteProduct)
    print(allob)
    context_product = {'concrete_products': allob}
    template = 'index.html'
    return render(request, template_name=template, context=context_product)


class Home(View):
    pass
