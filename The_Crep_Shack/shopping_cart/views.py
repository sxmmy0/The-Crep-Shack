from urllib import response
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from website.models import Product
from django.http import JsonResponse

# Create your views here.
def shopping_cart_summary(request):
    return render(request, "shopping_cart_summary.html", {})

def shopping_cart_add(request):
    #Get the cart
    cart = Cart(request)
    #Test for POST
    if request.POST.get('action') == 'post':
        #Get 
        product_id = int(request.POST.get('product_id'))
        #Lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #Save to session
        cart.add(product=product)
        #Return a response
        response = JsonResponse({'Product Name: ': product.name})
        return response

def shopping_cart_delete(request):
    pass

def shopping_cart_update(request):
    pass