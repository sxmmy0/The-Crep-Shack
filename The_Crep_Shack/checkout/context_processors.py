from .checkout import Checkout

def checkout(request):
    return{'cart': Checkout(request)}