from website.models import Product
from decimal import Decimal

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If 'session_key' doesn't exist or isn't a dictionary, initialize it as an empty dictionary
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of the site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        #Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = str(product_qty)

        self.session.modified = True
        


    def cart_total(self):
        # Get product IDS
        product_ids = self.cart.keys()
        # lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        # Start counting at 0
        total = Decimal('0.0')  # Intialise Decimal

        for key, value in quantities.items():
            # Convert key string into int so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    # Convert quantity to decimal if needed
                    value = Decimal(str(value))  # Optional conversion
                    if product.is_on_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value
        return total

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #Get IDs from cart
        product_ids = self.cart.keys()
        #use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)
        #return those looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        # Get Cart
        cart = self.cart
        #Update Cart
        cart[product_id] = product_qty
        
        self.session.modified = True
        
        object = self.cart
        return object
    
    def delete(self, product):
        product_id = str(product)
        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
    
    # def cart_total(self):
    #     # Get product IDS
    #     product_ids = self.cart.keys()
    #     # Lookup those keys in our products database model
    #     products = Product.objects.filter(id__in=product_ids)
    #     # Get quantities
    #     quantities = self.cart
    #     # Start counting at 0
    #     total = Decimal('0.0')  # Inicialize total como Decimal
        
    #     for key, value in quantities.items():
    #         # Convert key string into int so we can do math
    #         key = int(key)
    #         for product in products:
    #             if product.id == key:
    #                 qty = Decimal(value)  # Converta value para Decimal
    #                 if product.is_sale:
    #                     total += product.sale_price * qty
    #                 else:
    #                     total += product.price * qty
    #     return total