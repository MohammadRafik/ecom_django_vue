from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to='images/categorys',null=True, blank=True)
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
        verbose_name_plural = 'Categories'


    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.sub_categories_list = None

    def get_all_sub_categories(self):
        """
        Returns all sub categories from children
        """
        for sub_category in self.sub_categories_list:
            yield sub_category
            # Returns children of sub categories
            for sub_category2 in sub_category.get_all_sub_categories():
                yield sub_category2

    def get_sub_categories(self, categories):
        sub_categories = []
        for sub_category in categories:
            if sub_category.parent_id == self.id:
                sub_category.parent = self
                sub_categories.append(sub_category)

        return sub_categories

    @classmethod
    def get_category(cls, slug):
        """
        Returns category with sub categories
        """
        # Loads all categories along with sub categories list
        categories = list(cls.get_categories())

        for category in categories:
            if category.slug == slug:
                return category

    @classmethod
    def get_categories(cls):
        """
        Returns all categories active
        """
        categories = list(
            cls.objects.filter(is_active=True).order_by('display_order'))

        for category in categories:
            category.sub_categories_list = category.get_sub_categories(
                categories)
            category.sub_categories_count = len(category.sub_categories_list)

        return categories

class ProductImages(models.Model):
    display_order = models.IntegerField(default=0)
    image_url = models.ImageField(upload_to='images/products')
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

class Product(models.Model):
    title = models.CharField(max_length=250)    
    description = models.TextField(max_length=800, null=True, blank=True)
    catagory = models.ForeignKey(Category, on_delete=models.PROTECT)##########################################################################
    pictuer = models.ForeignKey(ProductImages, on_delete=models.CASCADE)############################################
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

