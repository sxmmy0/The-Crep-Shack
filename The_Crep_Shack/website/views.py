from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item, Order, OrderItem

# Create your views here.
# def home(request):
#     context = {"name": "Jordan 1"}
#     return render(request,"website/home.html", context)

def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "website/item_list.html", context)