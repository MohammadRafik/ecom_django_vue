from django.shortcuts import render
from django.views import View
from cart.models import Cart,CartItem

# Create your views here.
class CartPageLoader(View):

    def fetch_cart_data(self):
        self.cart = Cart.get_cart()


    def get(self, request):
        #what we need for this page it to enable it to be able to get all data from the carts, so
        #all the products, their costs and total cost, main photo of each product, and ability to remove items from the cart
        self.fetch_cart_data()
        return render(request, 'cart/home.html', {'cart':self.cart})



    def find_total_cart_items(self):
        pass