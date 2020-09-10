from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Service, Category, ConcreteProduct


def home(request):
    all_concrete_products = ConcreteProduct.objects.all()
    context = {'concrete_products': all_concrete_products}
    template = 'index.html'
    return render(request, template_name=template, context=context)


class Home(View):
    pass
