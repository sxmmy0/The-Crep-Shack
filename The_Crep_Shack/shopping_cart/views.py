from django.shortcuts import render

# Create your views here.
def shopping_cart_summary(request):
    return render(request, "shopping_cart_summary.html", {})

def shopping_cart_add(request):
    pass

def shopping_cart_delete(request):
    pass

def shopping_cart_update(request):
    pass