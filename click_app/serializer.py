from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('username', 'id')


class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer(serializers.PrimaryKeyRelatedField(many=False))

    class Meta:
        model = Product
        fields = ('name', 'price', 'owner', 'na_prodaje', 'time','expiration_date','image')
        read_only_fields = ('price',)

