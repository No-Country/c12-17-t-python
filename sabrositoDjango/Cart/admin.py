from django.contrib import admin
from .models import Product, Product_Order, Order

# Register your models here.

admin.site.register(Product_Order)
admin.site.register(Order)
admin.site.register(Product)