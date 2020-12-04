from .models import Cart

class CartManager():

    def __init__(self, request):
        if request.user.is_authenticated and 'cart_id' in request.session:
            # this means session of anon has a cart but now he logged in, so the cart should connect to the user, and if there is an old active cart for this user deactivate it
            try:
                cart = Cart.objects.get(user= request.user, active=True)
                cart.active = False
                cart.save()
                self.cart = Cart.objects.get(id = request.session['cart_id'], active=True)
                self.cart.user = request.user
                self.cart.save()
                request.session.pop('cart_id')
            except:
                self.cart = Cart.objects.get(id = request.session['cart_id'], active=True)
                self.cart.user = request.user
                self.cart.save()
                request.session.pop('cart_id')
        elif request.user.is_authenticated:
            try:
                self.cart = Cart.objects.get(user= request.user, active=True)
            except:
                self.cart = Cart(user = request.user)
                self.cart.save()
        elif 'cart_id' in request.session:
            try:
                self.cart = Cart.objects.get(id = request.session['cart_id'], active=True)
            except:
                request.session.pop('cart_id')
                self.cart = Cart()
                self.cart.save()
                request.session['cart_id'] = self.cart.id
        else:
            self.cart = Cart()
            self.cart.save()
            request.session['cart_id'] = self.cart.id
        self.load_items()

    def load_items(self):
        self.cart_items = self.cart.get_items()
        return self.cart_items

    def calc_quanitity(self):
        self.load_items()
        total_quantity = 0
        for cart_item in self.cart_items:
            total_quantity += cart_item.quantity
        return total_quantity

    def total_cost(self):
        self.total_cost = 0.0
        if hasattr(self, 'cart_items'):
            for cart_item in self.cart_items:
                self.total_cost += (float(cart_item.product.current_price) * cart_item.quantity)
            self.total_cost = round(self.total_cost, 2)
            self.tax = round(self.total_cost * 0.13, 2)
            self.total_cost_with_tax = round(self.total_cost + self.tax, 2)
            return (self.total_cost, self.tax, self.total_cost_with_tax)
        else:
            return 0

    def deactivate(self, request):
        if 'cart_id' in request.session:
            request.session.pop('cart_id')


        self.cart.active = False
        self.cart.save()
        return self.cart

    



