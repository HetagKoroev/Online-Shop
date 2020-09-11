from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Service, Category, ConcreteProduct
from .services.logic import get_all_model_objects


def home(request):
    context = {'concrete_products': get_all_model_objects(ConcreteProduct)}
    template = 'index.html'
    return render(request, template_name=template, context=context)


class Home(View):
    pass
