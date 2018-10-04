from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    discription = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=00.00)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)