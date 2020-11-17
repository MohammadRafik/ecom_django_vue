from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from cart.models import Cart,CartItem, CheckoutDetails
from products.models import ProductImage
from django.conf import settings
from django.contrib.auth.models import User, AnonymousUser
from cart.utils import CartManager
# Create your views here.



class CartPageLoader(View):
    def get(self, request):

        cart_manager = CartManager(request)
        cart_manager.load_items()
        cart_manager.total_cost()
        total_cost_for_stripe = cart_manager.total_cost_with_tax * 100

        # load product images
        product_images = []
        if hasattr(cart_manager, 'cart_items'):

            cart_product_ids = set()
            for cart_item in cart_manager.cart_items:
                cart_product_ids.add(cart_item.product.id)

            for cart_product_id in cart_product_ids:
                product_images.append(ProductImage.find_main_product_image(cart_product_id))


        # get stipe key
        stripe_key = settings.STRIPE_PUBLISHABLE_KEY


        return render(request, 'cart/home2.html', {'cart':cart_manager.cart, 'cart_items':cart_manager.cart_items, 'product_images':product_images, 'total_cost':cart_manager.total_cost,'tax':cart_manager.tax, 'total_cost_with_tax':cart_manager.total_cost_with_tax, 'stripe_key':stripe_key, 'total_cost_for_stripe':total_cost_for_stripe})


from cart.forms import CheckoutForm
class CheckoutLoader(View):
    checkout_template_name = 'cart/checkout_page.html'


    def get(self, request):
        form = CheckoutForm()
        return render(request, self.checkout_template_name, {'form':form})

    def post(self, request):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cart_manager = CartManager(request)
            cart_manager.load_items()
            cart_manager.total_cost()
            total_cost_for_stripe = cart_manager.total_cost_with_tax * 100
            
            stripe_key = settings.STRIPE_PUBLISHABLE_KEY

            user_name = request.user.get_username()

            # check if checkoutDetails object already exists, if yes update it, if no make one
            if CheckoutDetails.objects.filter(cart_id = cart_manager.cart.id).count():
                checkout_details = CheckoutDetails.objects.get(cart_id = cart_manager.cart.id)
                if 'userObject' in locals():
                    checkout_details.user = user.object
                checkout_details.cart = cart_manager.cart
                checkout_details.name_of_receiver = form.cleaned_data['name_of_receiver']
                checkout_details.main_address = form.cleaned_data['main_address']
                checkout_details.secondary_address = form.cleaned_data['secondary_address']
                checkout_details.city = form.cleaned_data['city']
                checkout_details.province = form.cleaned_data['province']
                checkout_details.postal_code = form.cleaned_data['postal_code']
                checkout_details.phone_number = form.cleaned_data['phone_number']
                checkout_details.updated_by = user_name
                checkout_details.created_by = user_name
                checkout_details.save()
            else:
                if 'userObject' in locals():
                    checkout_details = CheckoutDetails( user = request.user, cart = cart_manager.cart, name_of_receiver = form.cleaned_data['name_of_receiver'], main_address = form.cleaned_data['main_address'], secondary_address = form.cleaned_data['secondary_address'], city = form.cleaned_data['city'], province = form.cleaned_data['province'], postal_code = form.cleaned_data['postal_code'], phone_number = form.cleaned_data['phone_number'], updated_by = user_name, created_by = user_name)
                else:
                    checkout_details = CheckoutDetails(cart = cart_manager.cart, name_of_receiver = form.cleaned_data['name_of_receiver'], main_address = form.cleaned_data['main_address'], secondary_address = form.cleaned_data['secondary_address'], city = form.cleaned_data['city'], province = form.cleaned_data['province'], postal_code = form.cleaned_data['postal_code'], phone_number = form.cleaned_data['phone_number'], updated_by = user_name, created_by = user_name)
            checkout_details.save()


            return render(request, 'cart/make_payment.html', { 'form': form,'checkout_details':checkout_details, 'cart':cart_manager.cart, 'cart_items':cart_manager.cart_items, 'total_cost':cart_manager.total_cost,'tax':cart_manager.tax, 'total_cost_with_tax':cart_manager.total_cost_with_tax, 'stripe_key':stripe_key, 'total_cost_for_stripe':total_cost_for_stripe})
        else:
            return render(request, self.checkout_template_name, {'form':form})
            



            
def order_confirmation(request):
    cart_manager = CartManager(request)
    cart_manager.load_items()
    cart_manager.total_cost()
    total_cost_for_stripe = cart_manager.total_cost_with_tax * 100


    # load main image for each cart item product, should maybe redo this main img finder
    product_images =  []
    repeated = False
    if hasattr(cart_manager, 'cart_items'):
        for cart_item in cart_manager.cart_items:
            img_in_list = ProductImage.find_main_product_image(cart_item.product.id)
            repeated = False
            for product_image in product_images:
                if product_image.pk == img_in_list.pk:
                    repeated = True
                    break
            if not repeated:
                product_images.append(img_in_list)
                repeated = False

    if request.method == "GET":
        payment_confirmation = ''
    elif request.POST['payment_confirmation']:
        payment_confirmation = float(request.POST['payment_confirmation'])
    else:
        payment_confirmation = ''


    # deactivate this cart now
    cart_manager.deactivate(request)

    return render(request, 'cart/order_confirmation.html', {'cart':cart_manager.cart, 'cart_items':cart_manager.cart_items, 'product_images':product_images, 'total_cost':cart_manager.total_cost,'tax':cart_manager.tax, 'total_cost_with_tax':cart_manager.total_cost_with_tax, 'total_cost_for_stripe':total_cost_for_stripe, 'payment_confirmation':payment_confirmation, 'true_string':'True'})



def order_history(request):
    order_history = CheckoutDetails.objects.filter(user_id = request.user.id)
    cart_items_list = []
    product_images = []
    total_costs = []
    for order in order_history:
        cart_items = order.cart.get_items()
        cart_items_list.append(cart_items)
        #get product images
        repeated = False
        if cart_items:
            for cart_item in cart_items:
                img_in_list = ProductImage.find_main_product_image(cart_item.product.id)
                repeated = False
                for product_image in product_images:
                    if product_image.pk == img_in_list.pk:
                        repeated = True
                        break
                if not repeated:
                    product_images.append(img_in_list)
                    repeated = False
        #get order total cost
        total_cost = 0.0
        for cart_item in cart_items:
            total_cost += (float(cart_item.product.current_price) * cart_item.quantity)
        total_cost = round(total_cost, 2)
        total_cost_with_tax = total_cost*1.13
        total_cost_with_tax = round(total_cost_with_tax, 2)
        total_costs.append(total_cost_with_tax)

    order_cartitem_history = zip( order_history, cart_items_list, total_costs)
    return render(request, 'cart/order_history.html', {'orders':order_history, 'cart_items':cart_items, 'order_cartitem_history':order_cartitem_history, 'product_images':product_images})


def get_cart_items_count(request):
    cart_manager = CartManager(request)
    item_count_in_cart = cart_manager.cart.get_items_count()
    return HttpResponse(item_count_in_cart)


# ---------------------------------------------#
#-----------------rest framework---------------#
# ---------------------------------------------#
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