from django.contrib import admin

# Register your models here.
from .models import Product, Category, ProductImage, Supplier
# ,FeaturedProduct, FeaturedProductImage

admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
# admin.site.register(FeaturedProduct)
# admin.site.register(FeaturedProductImage)
