from django.db import models
from django.conf import settings
from decimal import Decimal
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0) #0 рублей
    quantite = models.IntegerField(default=1)


    def __str__(self): # Для отображения в админке name
        return self.name

    def get_price(self):
        return self.price * self.quantite

    def get_descriptions(self):
        return self.description

# class Orders(models.Model):
#     order = models.ForeignKey(to=Item, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f'Orders'
#
#     def sum(self):
#         return self.order.price * self.quantite
