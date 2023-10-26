from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category, Order, Product, Customer

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "content/home.html", {'products':products})

