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
            return cls.objects.filter(cart_id = cart_id)
        else:
            cart = cls()
            cart.save()
            return cart


    def create_cart_item(self, product_id, quantity, user='Anonymous'):
        #first check if this cart item already exists
        the_cart_item = self.cart_item.filter(cart_id=self.cart_id, product_id = product_id)
        if the_cart_item:
            the_cart_item.update_quantity(quantity)
            return the_cart_item
        else:
            the_cart_item = self.cart_item(product_id=product_id,quantity=quantity,updated_by=str(user),created_by=str(user))
            the_cart_item.save()
            return the_cart_item


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_item', on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
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

    def update_quantity(self, quantity):
        self.update(quantity=quantity)
