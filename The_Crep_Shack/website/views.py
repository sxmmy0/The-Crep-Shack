from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category, Order, Product, Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "content/home.html", {'products':products})

def about(request):
    return render(request, "content/about.html", {})

def login_user(request):
    return render(request, "content/login.html", {})

def logout_user(request):
    pass