from django.db import models
from django.db.models import Min
from tools.data_structures import Tree

# Create your models here.

class Supplier(models.Model):
    company_name = models.CharField(max_length=40)
    description = models.CharField(max_length=1600)
    contact_email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    full_address = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name



class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)#maybe delete this 
    description = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to='static/images/categorys',null=True, blank=True)
    parent = models.ForeignKey('self', related_name='sub_categories', null=True, blank=True, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100, null=True, blank=True, help_text='SEO keywords')
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_expended = models.BooleanField(default=False, help_text='Catergory will always shown expended')
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        ordering = ('display_order', 'id',)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.sub_categories_list = None

    def __str__(self):
        return self.name

    @classmethod
    def get_all_categories(cls):
        return cls.objects.filter(is_active = True)

    @classmethod
    def update_sub_category_lists(cls):
        all_categories = cls.get_all_categories()
        for single_category in all_categories:
            sub_categories = []
            for one_category in all_categories:
                if one_category.parent_id == single_category.id:
                    sub_categories.append(one_category)
            single_category.sub_categories_list = sub_categories
        return all_categories

    @staticmethod
    def find_main_categories(categories):
        # find value of lowest display order
        min_display_order = 324234
        for category in categories:
            if category.display_order < min_display_order:
                min_display_order = category.display_order
        # find and then return main categories
        main_categories = []
        for category in categories:
            if category.display_order == min_display_order:
                main_categories.append(category)
        return main_categories

    @classmethod
    def generate_navigation_code(cls, category,f):
        string_category = str(category)
        f.write( '''<dropdown :trigger="'hover'" :align="'right'">''')
        f.write( '''<template slot="btn"><a href="#" >'''+  string_category + '''</a></template>''' )
        # f.write( '''<template slot="btn"><a href="#">category</a></template>''' )
        f.write( '''<template slot="body">''' )
        if category.sub_categories_list != None:
            for child in category.sub_categories_list:
                cls.generate_navigation_code(child,f)
        f.write( '</template>' )
        f.write( '</dropdown>' )

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=800, null=True, blank=True)
    catagory = models.ForeignKey(Category, on_delete=models.PROTECT)##########################################################################
    product_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default='pepega')#################################################################
    current_price = models.DecimalField(max_digits=9,decimal_places=2)
    base_price = models.DecimalField(max_digits=9,decimal_places=2)
    cost = models.DecimalField(max_digits=9,decimal_places=2,default=0)
    quantity = models.IntegerField()
    tags = models.CharField(max_length=250, null=True, blank=True, help_text='keywords to help with searching and SEO')
    weight = models.FloatField(default=0)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class ProductImage(models.Model):
    display_order = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)############################################
    image_url = models.ImageField(upload_to='static/images/products')
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.product.title



