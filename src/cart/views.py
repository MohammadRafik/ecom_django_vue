from django.shortcuts import render
from django.views import View
from cart.models import Cart,CartItem, CheckoutDetails
from products.models import ProductImage
from django.conf import settings

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

        # calculate total cost
        total_cost = 0.0
        if cart_items:
            for cart_item in cart_items:
                total_cost += (float(cart_item.product.current_price) * cart_item.quantity)
        total_cost = round(total_cost, 2)
        tax = total_cost*0.13
        tax = round(tax, 2)
        total_cost_with_tax = total_cost*1.13
        total_cost_with_tax = round(total_cost_with_tax, 2)
        total_cost_for_stripe = total_cost_with_tax*100


        # get stipe key
        stripe_key = settings.STRIPE_PUBLISHABLE_KEY


        return render(request, 'cart/home.html', {'cart':self.cart, 'cart_items':cart_items, 'product_images':product_images, 'total_cost':total_cost,'tax':tax, 'total_cost_with_tax':total_cost_with_tax, 'stripe_key':stripe_key, 'total_cost_for_stripe':total_cost_for_stripe})



    def find_total_cart_items(self):
        pass

    @classmethod
    def delete_expired_carts(cls):
        pass

def order_confirmation(request):
    cart = Cart.get_cart(request.session['cart_id'])
    for the_cart in cart:
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

    # calculate total cost
    total_cost = 0.0
    if cart_items:
        for cart_item in cart_items:
            total_cost += (float(cart_item.product.current_price) * cart_item.quantity)
    total_cost = round(total_cost, 2)
    tax = total_cost*0.13
    tax = round(tax, 2)
    total_cost_with_tax = total_cost*1.13
    total_cost_with_tax = round(total_cost_with_tax, 2)
    total_cost_for_stripe = total_cost_with_tax*100


    # clear out cart session and make new cart
    new_cart = Cart.get_cart()
    for one_cart in new_cart:
        request.session['cart_id'] = one_cart.id
    return render(request, 'cart/order_confirmation.html', {'cart':cart, 'cart_items':cart_items, 'product_images':product_images, 'total_cost':total_cost,'tax':tax, 'total_cost_with_tax':total_cost_with_tax, 'total_cost_for_stripe':total_cost_for_stripe})






class CheckoutLoader(View):

    def get(self, request):

        return render(request, 'cart/checkout_page.html', {})

























from rest_framework import viewsets
from .serializers import CartItemSerializer, CartSerializer, CheckoutDetailsSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CheckoutDetailsViewSet(viewsets.ModelViewSet):
    queryset = CheckoutDetails.objects.all()
    serializer_class = CheckoutDetailsSerializer