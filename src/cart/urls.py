from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.CartPageLoader.as_view(), name='cartpageloader'),
    path('confirmation', views.order_confirmation, name='order_confirmation'),
    path('checkout', views.CheckoutLoader.as_view(), name='checkout_page'),
    path('order_history', views.order_history, name='order_history'),
    path('get_cart_items_count', views.get_cart_items_count, name='get_cart_items_count'),

]
