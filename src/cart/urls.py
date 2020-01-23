from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.CartPageLoader.as_view(), name='cartpageloader'),
    path('confirmation', views.order_confirmation, name='order_confirmation'),
    path('checkout', views.CheckoutLoader.as_view(), name='checkout_page'),

]
