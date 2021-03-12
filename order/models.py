from django.db import models

from store.models import Product
# Create your models here.



    
    
class Order(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True, max_length=200)
    zipcode = models.CharField(max_length=100, null=True)
    
    place = models.CharField(max_length=100, null=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)
    
    
    def __str__(self):
        return self.first_name
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="items")
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    