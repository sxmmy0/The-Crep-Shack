from django.db import models
from website.models import Product

class Checkout():
    def __init__(self, request):
        self.session = request.session
        checkout = self.session.get('session_key')
        if 'session_key' not in request.session:
            checkout = self.session['session_key'] = {}
        self.checkout = checkout

    def get_prods(self):
        #Get IDs from cart
        product_ids = self.checkout.keys()
        #use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)
        #return those looked up products
        return products