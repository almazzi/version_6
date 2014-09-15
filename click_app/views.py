from django.shortcuts import render
from django.views.generic import ListView
from click_app.models import Product


class ProductNaProdaje(ListView):
    template_name = "click_app/index.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(na_prodaje="True")







# Create your views here.
