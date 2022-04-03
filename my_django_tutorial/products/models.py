from operator import truediv
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    #description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default="this is cool!")
    feature = models.BooleanField(default=False)

    def getAbsolutePathItem(self):
        return f"/product/{self.id}/"