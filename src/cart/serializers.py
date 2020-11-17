from rest_framework import serializers
from .models import CartItem, Cart, CheckoutDetails

class CartItemSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = CartItem
        fields = ( 'id', 'url', 'cart', 'product', 'quantity', 'updated_by', 'updated_on', 'created_on', 'created_by' )


class CartSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Cart
        fields = ('id', 'url', 'active', 'updated_by', 'updated_on', 'created_on', 'created_by')


class CheckoutDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckoutDetails
        fields = ('id', 'url', 'cart', 'name_of_receiver', 'main_address', 'secondary_address', 'city', 'province', 'postal_code', 'phone_number', 'updated_by', 'updated_on', 'created_on', 'created_by')