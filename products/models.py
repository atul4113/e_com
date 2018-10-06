from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    discription = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=00.00)
    sale_price = models.DecimalField(max_digits=10,decimal_places=2, default=00.00,null=True,blank=True)
    image = models.FileField(upload_to='products/images',null=True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=True)
    image = models.ImageField(upload_to='product/image/')
    thambnail = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
