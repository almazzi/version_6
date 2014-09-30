from django.contrib import admin
from click_app.models import Product
from django import forms


class ProductAdmin(admin.ModelAdmin):
    exclude = ('na_prodaje',)

admin.site.register(Product, ProductAdmin)
# Register your models here.
