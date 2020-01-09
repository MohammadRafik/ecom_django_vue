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

    # i think filter can be accessed from request.filter so i dont think i need to pass it in like this..?
    def get(self, request, filter = ''):
        self.all_categories = Category.update_sub_category_lists()
        self.categories = Category.find_main_categories(self.all_categories)



        # here we use the filter to load the products accordingly!
        if filter != '':
            self.category_from_filter = list(Category.objects.filter(name = filter))
            self.list_of_all_categories_from_filter = Category.get_all_sub_categories(self.category_from_filter[0])
            self.list_of_all_categories_from_filter.append(self.category_from_filter[0])
            self.all_products = Product.get_products_from_list_of_categories(self.list_of_all_categories_from_filter)
        else:
            self.all_products = Product.get_all_products()



        #now we find all the images we need for each product
        self.all_product_images = []
        for product in self.all_products:
            img = list(ProductImage.find_all_product_images(product.id))
            self.all_product_images += img


        # this should be to load the homepage, so give featured products and catalog data
        return render(request, 'products/home.html', {'main_categories':self.categories, 'all_categories':self.all_categories, 'products':self.all_products, 'product_images':self.all_product_images })




def product_page(request, product_id):
    #find product and give it to template
    main_product = list(Product.objects.filter(id = product_id))
    main_product = main_product[0]
    main_image = list(ProductImage.find_main_product_image(product_id))
    main_image = main_image[0]
    other_images = ProductImage.find_product_images(product_id)

    return render(request, 'products/product.html', {'product':main_product, 'main_image':main_image, 'other_images':other_images})







from django.db.models import Q
import re
########################################
#########product searching##############
########################################

def normalize_query(query_string,
    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
    normspace=re.compile(r'\s{2,}').sub):

    '''
    Splits the query string in invidual keywords, getting rid of unecessary spaces and grouping quoted words together.
    Example:
    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    '''

    return [normspace(' ',(t[0] or t[1]).strip()) for t in findterms(query_string)]



def get_query(query_string, search_fields):

    '''
    Returns a query, that is a combination of Q objects. 
    That combination aims to search keywords within a model by testing the given search fields.
    '''

    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search_for_something(request):
    query_string = ''
    found_entries = None

    if ('search_string' in request.GET) and request.GET['search_string'].strip():
        query_string = request.GET['search_string']
        entry_query = get_query(query_string, ['description', 'tags', 'title'])
        found_entries = Product.objects.filter(entry_query)

    return found_entries


def product_search(request):
    all_categories = Category.update_sub_category_lists()
    categories = Category.find_main_categories(all_categories)

    found_products = search_for_something(request)

    all_product_images = []
    for product in found_products:
        img = list(ProductImage.find_all_product_images(product.id))
        all_product_images += img

    return render(request, 'products/home.html', {'main_categories':categories, 'all_categories':all_categories, 'products':found_products, 'product_images':all_product_images })


















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