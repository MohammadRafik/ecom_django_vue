from django.shortcuts import render
from django.views import View
from cart.models import Cart,CartItem
from products.models import ProductImage

# Create your views here.



def get_cart(request):
    if 'cart_id' in request.session:
        cart = Cart.get_cart(request.session['cart_id'])
    else:
        cart = Cart.get_cart()
        for cart2 in cart:
            request.session['cart_id'] = cart2.id
    return cart


class CartPageLoader(View):




    def get(self, request):
        #what we need for this page it to enable it to be able to get all data from the carts, so
        #all the products, their costs and total cost, main photo of each product, and ability to remove items from the cart
        if 'cart_id' in request.session:
            self.cart = Cart.get_cart(request.session['cart_id'])
        else:
            self.cart = Cart.get_cart()
            for cart in self.cart:
                request.session['cart_id'] = cart.id
        for the_cart in self.cart:
            cart_items = the_cart.get_items()
        # load main image for each cart item product
        product_images =  []
        repeated = False
        if cart_items:
            for cart_item in cart_items:
                img_in_list = list(ProductImage.find_main_product_image(cart_item.product.id))
                repeated = False
                for product_image in product_images:
                    if product_image.pk == img_in_list[0].pk:
                        repeated = True
                        break
                if not repeated:
                    product_images += img_in_list
                    repeated = False






        return render(request, 'cart/home.html', {'cart':self.cart, 'cart_items':cart_items, 'product_images':product_images})



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
