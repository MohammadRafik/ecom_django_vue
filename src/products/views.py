from django.shortcuts import render
from django.views import View
from products.models import Category, Supplier, Product, ProductImage
import os
from rest_framework import viewsets
from .serializers import CategorySerializer, SupplierSerializer, ProductSerializer, ProductImageSerializer


# this class is used to find all catagorys in the database bring them
# in, and check if a catagory is selected and load things accordingly
class BaseLoader(View):

    @classmethod
    def generate_navigation_code(cls, category,f):
        string_category = str(category)
        if category.sub_categories_list != []:
            f.write( '''<dropdown :trigger="'hover'" :align="'right'">''')
            f.write( '''<template slot="btn"><a href="#" v-on:click="update_category(' '''+  string_category + ''' ')">'''+  string_category + '''</a></template>''' )
            # f.write( '''<template slot="btn"><a href="#">category</a></template>''' )
            f.write( '''<template slot="body">''' )
            if category.sub_categories_list != []:
                for child in category.sub_categories_list:
                    cls.generate_navigation_code(child,f)
            f.write( '</template>' )
            f.write( '</dropdown>' )
        else:
            f.write( '''<li><a href="#">''' + string_category + '''</a></li> ''')

    # def __init__(self):



    def get(self, request):
        # generate html code to list all categories
        self.all_categories = Category.update_sub_category_lists()
        self.categories = Category.find_main_categories(self.all_categories)
        path = os.getcwd() + '\src\products\\navigationString.txt'
        try:
            f= open(path,"w+")
        except:
            path = os.getcwd() + '\products\\navigationString.txt'
            f= open(path,"w+")
            
        if 'category' not in request.session:
        # if True:
        # if False:
            f.write(''' 
                        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
                        <div class="sidebar-sticky">
                        <h5 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
                        Navigation
                        </h5>
                        <ul class="nav flex-column">
                    ''')
            for cat in self.categories:
                self.generate_navigation_code(cat, f)
            f.write(''' 
                        </ul>
                        </div>
                        </nav> 
                    ''')
            f.close()
        else:
            f.write('''
                        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
                        <div class="sidebar-sticky">
                        <ul class="nav flex-column">
                        <dropdown :trigger="'hover'" :align="'right'">
                        <template slot="btn"><a href="#" >Catalog</a></template>
                        <template slot="body">
                    ''')
            for cat in self.categories:
                self.generate_navigation_code(cat, f)
            f.write('''
                        </ul>
                        </div>
                        </nav>
                        </template>
                        </dropdown>
                    ''')
            f.close()

        with open(path, 'r') as file:
            self.massive_string = file.read().replace('\n', '')
            f.close()
    # this should be to load the homepage, so give featured products and catalog data
        return render(request, 'products/home.html', {'categories':self.categories, 'all_categories':self.all_categories, 'massive_string':self.massive_string})


#these are for setting up the api for all the models using the django rest framework
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

