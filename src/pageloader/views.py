from django.shortcuts import render
from django.views import View
from products.models import Category
import os

# Create your views here.
class BaseLoader(View):
    # this class is used to find all catagorys in the database bring them
    # in, and check if a catagory is selected and load things accordingly

    @classmethod
    def tree_traversal(cls, category,f):
        string_category = str(category)
        f.write( '''<dropdown :trigger="'hover'" :align="'right'">''')
        f.write( '''<template slot="btn"><a href="#">'''+  string_category + '''</a></template>''' )
        # f.write( '''<template slot="btn"><a href="#">category</a></template>''' )
        f.write( '''<template slot="body">''' )
        if category.sub_categories_list != None:
            for child in category.sub_categories_list:
                cls.tree_traversal(child,f)
        f.write( '</template>' )
        f.write( '</dropdown>' )

    def __init__(self):
        self.all_categories = Category.update_sub_category_lists()
        self.categories = Category.find_main_categories(self.all_categories)
        path = os.getcwd() + '\src\pageloader\\navigationString.txt'
        f= open(path,"w+")
        for cat in self.categories:
            self.tree_traversal(cat, f)
        f.close()

        with open(path, 'r') as file:
            self.massive_string = file.read().replace('\n', '')
            f.close()
        
    def get(self, request):
    # this should be to load the homepage, so give featured products and catalog data
        return render(request, 'pageloader/home.html', {'categories':self.categories, 'all_categories':self.all_categories, 'massive_string':self.massive_string})