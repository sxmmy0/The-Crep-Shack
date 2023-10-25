from django.db import models
from django.conf import settings
import datetime

# Create your models here.

# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):

    def __str__(self):
        return self.title
    
class Order(models.Model):
    pass
