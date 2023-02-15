from django.contrib import admin
from .models import Item
# Register your models here.
admin.site.register(Item) # Регистрации нашей модели Item в админке
#
# admin.site.register(Orders)