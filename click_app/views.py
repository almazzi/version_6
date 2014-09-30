from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from click_app.models import Product
from click_app.serializer import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from datetime import datetime

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    """
    Retrieve, update or delete a Product instance.
    """
    try:
        product = Product.objects.get(na_prodaje=True)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def flipDetail(request, pk):
    """
   Retrieve, update or delete a snippet instance.
   """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductNaProdaje(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(na_prodaje="True")


@api_view(['GET', 'POST'])
def product_list(request, format=None):
    """
  List all snippets, or create a new snippet.
  """
    if request.method == 'GET':
        product = Product.objects.filter(na_prodaje=True)

        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










# Create your views here.
