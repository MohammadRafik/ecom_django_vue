from django.db import models
from products.models import Product


# Create your models here.
#add functionality to be able to remove a cartItem, or change its quantity
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def find_cost(self):
        self.current_price = self.product.current_price
        tax = 1.12
        self.total_cost = self.quantity * self.current_price * tax



class Cart(models.Model):
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

