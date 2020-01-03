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

    def find_total_cost(self):
        current_price = self.product.current_price
        tax = 1.12
        self.total_cost = self.quantity * current_price * tax
        return self.total_cost

    def find_item_price(self):
        return self.product.current_price

    def update_quantity(self, product_id, quantity):
        self.filter(product_id=product_id).update(quantity=quantity)



class Cart(models.Model):
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

