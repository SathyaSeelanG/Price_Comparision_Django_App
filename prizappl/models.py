from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    amazon_url = models.URLField()
    amazon_price = models.FloatField()
    flipkart_url = models.URLField()
    flipkart_price = models.FloatField()
