from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=70)
    banner = models.ImageField()

    def __str__(self):
        return self.title
    
class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)    
