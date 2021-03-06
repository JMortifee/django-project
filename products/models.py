from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, 
    null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category',
    null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    date = models.DecimalField(max_digits=4, 
    decimal_places=0)
    price = models.DecimalField(max_digits=6, 
    decimal_places=2)
    width = models.DecimalField(max_digits=6, 
    decimal_places=0)
    height = models.DecimalField(max_digits=6, 
    decimal_places=0)
    image = models.ImageField(null=True, blank=True)
    quantity = models.DecimalField(max_digits=6, 
    decimal_places=0)

    def __str__(self):
        return self.name