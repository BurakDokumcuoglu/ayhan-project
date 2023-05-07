from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    unitsInStock = models.IntegerField()
    
    def _str_(self):
        return self
    

