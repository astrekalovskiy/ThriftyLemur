from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name