from django.db import models

# Create your models here.

class Logo(models.Model):
    title = models.CharField(max_length=120)
    logo_img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    sub_cat = models.ForeignKey('self', related_name = "subs", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=100, null="True")

    
    def __str__(self):
        return self.title




class Product(models.Model):
    title = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(max_length=350, null=True, blank=True)
    parent = models.ForeignKey('self', related_name="variants", on_delete=models.CASCADE, null=True, blank=True)
    uoms = models.ForeignKey('self', related_name="ums", on_delete=models.CASCADE, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    short_desc = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title    