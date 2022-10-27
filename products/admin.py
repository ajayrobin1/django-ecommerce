from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
