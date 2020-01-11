from django.shortcuts import render
from django.views import View
from cart.models import Cart,CartItem

# Create your views here.
class CartPageLoader(View):




    def get(self, request):
        #what we need for this page it to enable it to be able to get all data from the carts, so
        #all the products, their costs and total cost, main photo of each product, and ability to remove items from the cart
        if 'cart_id' in request.session:
            self.cart = Cart.get_cart(request.session['cart_id'])
        else:
            self.cart = Cart.get_cart()
            request.session['cart_id'] = self.cart.id
        return render(request, 'cart/home.html', {'cart':self.cart})



    def find_total_cart_items(self):
        pass

    @classmethod
    def delete_expired_carts(cls):
        pass

from rest_framework import viewsets
from .serializers import CartItemSerializer, CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer