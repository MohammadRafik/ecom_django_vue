from django.shortcuts import render
from django.views import View
from products.models import Category

# Create your views here.
class BaseLoader(View):
    # this class is used to find all catagorys in the database bring them
    # in, and check if a catagory is selected and load things accordingly

    def __init__(self):
        self.categories = Category.get_main_categories()
        self.sub_cate = []
        for main_categories in self.categories:
            x = main_categories.get_all_sub_categories()
            self.sub_cate.append(x)

    def get(self, request):
    # this should be to load the homepage, so give featured products and catalog data
        return render(request, 'pageloader/home.html', {'categories':self.categories, 'sub_categories':self.sub_cate})