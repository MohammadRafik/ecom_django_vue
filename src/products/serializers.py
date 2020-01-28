from rest_framework import serializers
from .models import Category, Supplier, Product, ProductImage, FeaturedProduct, FeaturedProductImage

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'company_name', 'description', 'contact_email', 'phone_number', 'full_address', 'updated_by', 'updated_on', 'created_on', 'created_by' )


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ( 'id', 'url', 'name', 'slug', 'description', 'image_url', 'parent', 'tags', 'display_order', 'is_active', 'updated_by', 'updated_on', 'created_on', 'created_by' )

class ProductSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Product
        fields = ( 'id', 'title', 'description', 'category', 'product_supplier', 'current_price', 'base_price', 'cost', 'quantity', 'tags', 'weight', 'length', 'width', 'height', 'updated_by', 'updated_on', 'created_on', 'created_by' )

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductImage
        fields = ( 'id', 'product', 'image_url', 'main_picture',  'updated_by', 'updated_on', 'created_on', 'created_by')




# featured items serializer


# class FeaturedProductSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = FeaturedProduct
#         fields = ( 'id', 'title', 'description', 'category', 'product_supplier', 'current_price', 'base_price', 'cost', 'quantity', 'tags', 'weight', 'length', 'width', 'height', 'updated_by', 'updated_on', 'created_on', 'created_by' )

# class FeaturedProductImageSerializer(serializers.HyperlinkedModelSerializer):
    
#     class Meta:
#         model = FeaturedProductImage
#         fields = ( 'id', 'featured_product', 'image_url', 'main_picture',  'updated_by', 'updated_on', 'created_on', 'created_by')