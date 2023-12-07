from urllib import response
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from website.models import Product
from django.http import JsonResponse, HttpResponse

# Create your views here.
def cart_summary(request):
    #Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "cart_summary.html", {"cart_products":cart_products})

def cart_add(request):
    #Get the cart
    cart = Cart(request)
    #Test for POST
    if request.POST.get('action') == 'post':

        #Get Product ID
        product_id = int(request.POST.get('product_id'))

        # Lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        
        # Save to session
        cart.add(product=product)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return a response
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass