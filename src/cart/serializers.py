from rest_framework import serializers
from .models import CartItem, Cart

class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = ( 'id', 'product_id', 'quantity', 'updated_by', 'updated_on', 'created_on', 'created_by' )


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'updated_by', 'updated_on', 'created_on', 'created_by')
