from rest_framework import serializers
from .models import CartItem, Cart

class CartItemSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = CartItem
        fields = ( 'id', 'url', 'cart', 'product', 'quantity', 'updated_by', 'updated_on', 'created_on', 'created_by' )


class CartSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Cart
        fields = ('id','url', 'updated_by', 'updated_on', 'created_on', 'created_by')
