from rest_framework import serializers
from .models import Category, Supplier, Product, ProductImage

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'company_name', 'description', 'contact_email', 'phone_number', 'full_address', 'updated_by', 'updated_on', 'created_on', 'created_by' )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ( 'name', 'slug', 'description', 'image_url', 'parent_id', 'tags', 'display_order', 'is_active', 'updated_by', 'updated_on', 'created_on', 'created_by' )

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'title', 'description', 'catagory_id', 'product_supplier_id', 'current_price', 'base_price', 'cost', 'quantity', 'tags', 'weight', 'length', 'width', 'height', 'updated_by', 'updated_on', 'created_on', 'created_by' )

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        fields = ( 'id', 'display_order', 'product_id', 'image_url',  'updated_by', 'updated_on', 'created_on', 'created_by')

