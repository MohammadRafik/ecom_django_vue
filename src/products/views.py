from django.shortcuts import render
from django.views import View
from products.models import Category, Supplier, Product, ProductImage
import os
from rest_framework import viewsets
from .serializers import CategorySerializer, SupplierSerializer, ProductSerializer, ProductImageSerializer


# this class is used to find all catagorys in the database bring them
# in, and check if a catagory is selected and load things accordingly
class BaseLoader(View):

    def __init__(self):
        # generate code to list all categories
        self.all_categories = Category.update_sub_category_lists()
        self.categories = Category.find_main_categories(self.all_categories)
        path = os.getcwd() + '\src\products\\navigationString.txt'
        try:
            f= open(path,"w+")
        except:
            path = os.getcwd() + '\products\\navigationString.txt'
            f= open(path,"w+")
        for cat in self.categories:
            Category.generate_navigation_code(cat, f)
        f.close()

        with open(path, 'r') as file:
            self.massive_string = file.read().replace('\n', '')
            f.close()
        
        #get all products that belong to the currently selected section



    def get(self, request):
    # this should be to load the homepage, so give featured products and catalog data
        return render(request, 'products/home.html', {'categories':self.categories, 'all_categories':self.all_categories, 'massive_string':self.massive_string})


#serilazerationzzzz
class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer