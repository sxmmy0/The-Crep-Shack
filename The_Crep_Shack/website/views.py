from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    context = {"name": "Jordan 1"}
    return render(request,"website/home.html", context)