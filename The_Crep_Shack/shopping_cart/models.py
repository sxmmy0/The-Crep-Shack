from django.db import models
from website.models import Product

# Create your models here.

# class ShoppingCart(models.Model):
#     products = models.ManyToManyField(Product, blank=True)
#     total = models.DecimalField(max_digits=6, decimal_places=2, default=0) # type: ignore
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     active = models.BooleanField(default=True)

#     def __unicode__(self):
#         return "ShoppingCart id: %s" %(self.id)