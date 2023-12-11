from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Category, Order, Product, Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def product_category(request, product_id):
    # Retrieve the product object based on the product_id
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        # Handle the case where the product does not exist (e.g., show a 404 page)
        return render(request, '404.html')

    # Render the product detail template, passing the product object
    return render(request, 'product.html', {'product': product})

def category(request, title):
    # Replace hyphens with spaces
    title = title.replace('-', ' ')
    # Grab category from url
    try:
        # look up category
        category = Category.objects.get(name=title)
        products = Product.objects.filter(category=category)
        return render(request, "content/category.html", {"products": products, "category": category})
    except:
        messages.success(request, ("That category does not exist!"))
        return redirect('home')


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "content/product.html", {'product': product})


def home(request):
    products = Product.objects.all()
    return render(request, "content/home.html", {'products': products})


def about(request):
    return render(request, "content/about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            messages.success(
                request, ("There was an error logging you in, please try again!"))
            return redirect('login')
    else:
        return render(request, "content/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('home')


def register_user(request):
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, ("You have successfully registered a new account!"))
            return redirect('home')
        else:
            messages.success(
                request, ("There was an error registering your new account, please try again!"))
            return redirect('register')
    else:
        return render(request, "content/register.html", {'form': form})

def privacy(request):
    return render(request, "content/privacy.html", {})

def terms(request):
    return render(request, "content/terms.html", {})

def faq(request):
    return render(request, "content/faq.html", {})

def all_products(request):
    products = Product.objects.all()
    return render(request, "content/all_products.html", {'products': products})