class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If 'session_key' doesn't exist or isn't a dictionary, initialize it as an empty dictionary
        if not isinstance(cart, dict):
            cart = {}
            self.session['session_key'] = cart

        # Make sure cart is available on all pages of the site
        self.cart = cart
