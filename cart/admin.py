from django.contrib import admin

# Register your models here.
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cart, CartAdmin)
