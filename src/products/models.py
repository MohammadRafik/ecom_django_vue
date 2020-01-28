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
    slug = models.SlugField(max_length=20, unique=True)#delete this 
    description = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to='images/categories',null=True, blank=True)
    parent = models.ForeignKey('self', related_name='sub_categories', null=True, blank=True, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100, null=True, blank=True, help_text='SEO keywords')
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_expended = models.BooleanField(default=False, help_text='Catergory will always shown expended') #delete this
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

    # maybe refactor this abomination later?
    def get_all_sub_categories(self):
        all_categories = self.update_sub_category_lists()
        for cat in all_categories:
            if cat.id == self.id:
                category = cat
                break

        def traverse_tree(category):
            if  category.sub_categories_list != None:
                for sub_category in category.sub_categories_list:
                    traverse_tree(sub_category)
                    yield sub_category
        generator_with_sub_categories = traverse_tree(category)

        list_of_all_sub_categories = []
        for x in generator_with_sub_categories:
            list_of_all_sub_categories.append(x)
        return list_of_all_sub_categories


    

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=800, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)##########################################################################
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


    # def return_all_child_categories(self):
    #     return self.category.get_all_sub_categories()

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()

    @classmethod
    def get_products_by_category_id(cls, category_id):
        return cls.objects.filter(category_id = category_id)


    @classmethod
    def get_products_from_list_of_categories(cls, list_of_category_and_all_its_sub_categories):
        products = []
        for single_category in list_of_category_and_all_its_sub_categories:
            product = list(cls.objects.filter(category = single_category))
            products = products + product
        return products





class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)############################################
    image_url = models.ImageField(upload_to='images/products')
    main_picture = models.BooleanField(default=False)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.product.title

    @classmethod
    def find_product_images(cls, product_id):
        return cls.objects.filter(product_id = product_id,  main_picture = False)

    @classmethod
    def find_main_product_image(cls, product_id):
        return cls.objects.filter(product_id = product_id, main_picture = True)

    @classmethod
    def find_all_product_images(cls, product_id):
        return cls.objects.filter(product_id = product_id)





# class FeaturedProduct(models.Model):
#     title = models.CharField(max_length=250)
#     description = models.TextField(max_length=800, null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)##########################################################################
#     product_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default='pepega')#################################################################
#     current_price = models.DecimalField(max_digits=9,decimal_places=2)
#     base_price = models.DecimalField(max_digits=9,decimal_places=2)
#     cost = models.DecimalField(max_digits=9,decimal_places=2,default=0)
#     quantity = models.IntegerField()
#     tags = models.CharField(max_length=250, null=True, blank=True, help_text='keywords to help with searching and SEO')
#     weight = models.FloatField(default=0)
#     length = models.FloatField(default=0)
#     width = models.FloatField(default=0)
#     height = models.FloatField(default=0)
#     updated_by = models.CharField(max_length=100)
#     updated_on = models.DateTimeField(auto_now=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     created_by = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title


#     # def return_all_child_categories(self):
#     #     return self.category.get_all_sub_categories()

#     @classmethod
#     def get_all_products(cls):
#         return cls.objects.all()

#     @classmethod
#     def get_products_by_category_id(cls, category_id):
#         return cls.objects.filter(category_id = category_id)


#     @classmethod
#     def get_products_from_list_of_categories(cls, list_of_category_and_all_its_sub_categories):
#         products = []
#         for single_category in list_of_category_and_all_its_sub_categories:
#             product = list(cls.objects.filter(category = single_category))
#             products = products + product
#         return products



# class FeaturedProductImage(models.Model):
#     featured_product = models.ForeignKey(FeaturedProduct, on_delete=models.CASCADE)
#     image_url = models.ImageField(upload_to='images/featured_products')
#     main_picture = models.BooleanField(default=False)
#     updated_by = models.CharField(max_length=100)
#     updated_on = models.DateTimeField(auto_now=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     created_by = models.CharField(max_length=100)

#     def __str__(self):
#         return self.featured_product.title
 
#     @classmethod
#     def find_product_images(cls, product_id):
#         return cls.objects.filter(featured_product_id = product_id,  main_picture = False)

#     @classmethod
#     def find_main_product_image(cls, product_id):
#         return cls.objects.filter(featured_product_id = product_id, main_picture = True)

#     @classmethod
#     def find_all_product_images(cls, product_id):
#         return cls.objects.filter(featured_product_id = product_id)