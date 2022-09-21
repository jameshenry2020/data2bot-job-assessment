from django.db import models
from django.utils.translation import gettext_lazy as _

from customers.models import User

# Create your models here.

"""just a simple product store model that user can order for """
class Product(models.Model):
    name=models.CharField(max_length=100, verbose_name=(_("Product Name")))
    description=models.TextField()
    price=models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

"""this is the user orders for a specify product at a session, that is at a particular point"""
class Order(models.Model):
    product=models.ForeignKey(Product, null=True, blank=True, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=1)
    payment_method=models.CharField(max_length=50, null=True, blank=True)
    completed=models.BooleanField(default=False)# only completed order will be pass to ther Order table
    timestamp=models.DateTimeField(auto_now_add=True, null=True)


    def get_total_item_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name










