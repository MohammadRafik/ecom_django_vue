from django.db import models
from products.models import Product


# Create your models here.
#add functionality to be able to remove a cartItem, or change its quantity

class Cart(models.Model):

    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)


    @classmethod
    def get_cart(cls, cart_id=None):
        if cart_id:
            return cls.objects.filter(id = cart_id)
        else:
            cart = cls()
            cart.save()
            return cls.objects.filter(id = cart.id)

    def get_items(self):
        return self.cart_items.prefetch_related('product').all()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    updated_by = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.product.title + ' cart item from cart object ' + str(self.cart.id)

    def find_total_cost(self):
        current_price = self.product.current_price
        tax = 1.12
        self.total_cost = self.quantity * current_price * tax
        return self.total_cost

    def find_item_price(self):
        return self.product.current_price

    def update_quantity(self, quantity):
        self.update(quantity=quantity)
