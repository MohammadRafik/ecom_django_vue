from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    parent = models.ForeignKey('self', related_name='sub_categories', null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True, help_text='SEO keywords')
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_expended = models.BooleanField(default=False, help_text='Catergory will always shown expended')
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=250)    
    description = models.TextField(max_length=800, null=True, blank=True)
    catagory = models.ForeignKey(Category)##########################################################################
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

class ProductImages(models.Model):
    pass