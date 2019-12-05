from django.shortcuts import render
from django.views import View
from products.models import Category, Supplier, Product, ProductImage
import os
from rest_framework import viewsets
from .serializers import CategorySerializer, SupplierSerializer, ProductSerializer, ProductImageSerializer
from django.http import HttpRequest, HttpResponse

# this class is used to find all catagorys in the database bring them
# in, and check if a catagory is selected and load things accordingly
class BaseLoader(View):

    @classmethod
    def generate_navigation_code(cls, category,f):
        string_category = str(category)
        if category.sub_categories_list != []:
            f.write( '''<dropdown :trigger="'hover'" :align="'right'">''')
            f.write( '''<template slot="btn"><a href="{% url 'products:filter' %}" v-on:click="update_category(' '''+  string_category + ''' ')">{{ '''+  string_category + ''' }}'''+  string_category + '''</a></template>''' )
            # f.write( '''<template slot="btn"><a href="#">category</a></template>''' )
            f.write( '''<template slot="body">''' )
            if category.sub_categories_list != []:
                for child in category.sub_categories_list:
                    cls.generate_navigation_code(child,f)
            f.write( '</template>' )
            f.write( '</dropdown>' )
        else:
            f.write( '''<li><a href="#" v-on:click="update_category(' '''+  string_category + ''' ')" >''' + string_category + '''</a></li> ''')

    # def __init__(self):




    def get(self, request, filter = ''):
        # generate html code to list all categories
        self.all_categories = Category.update_sub_category_lists()
        self.categories = Category.find_main_categories(self.all_categories)
        path = os.getcwd() + '\src\products\\navigationString.txt'
        try:
            f= open(path,"w+")
        except:
            path = os.getcwd() + '\products\\navigationString.txt'
            f= open(path,"w+")
        # here we check if a category has been selected, if it has we display the catalog differently
        if filter == '':
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

        # now we use the filter to load the products accordingly!
        if filter != '':
            self.category_from_filter = list(Category.objects.filter(name = filter))
            self.list_of_all_categories_from_filter = Category.get_all_sub_categories(self.category_from_filter[0])
            self.list_of_all_categories_from_filter.append(self.category_from_filter[0])
            self.all_products = Product.get_products_from_list_of_categories(self.list_of_all_categories_from_filter)

        else:
            self.all_products = Product.get_all_products()




        # this should be to load the homepage, so give featured products and catalog data
        return render(request, 'products/home.html', {'categories':self.categories, 'all_categories':self.all_categories, 'massive_string':self.massive_string, 'products':self.all_products})



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





# simple session read write api to be used with axios
class SessionAccess(View):
    def get(self, request):
        index = request.GET['index']
        if index in request.session:
            return HttpResponse(request.session[index])
        else:
            return HttpResponse(False)


    def post(self, request):
        index = request.POST['index']
        value = request.POST['value']
        request.session[index] = value
        return HttpResponse(request.session[index])