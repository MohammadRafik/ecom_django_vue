from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        # not able to add parent, which is very important and needed D:
        fields = ('id', 'name', 'slug', 'description', 'image_url', 'tags', 'display_order', 'is_active', 'updated_by', 'updated_on', 'created_on', 'created_by')