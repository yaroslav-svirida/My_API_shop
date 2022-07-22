from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import *

class UserCreateCustomSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email', 'first_name', 'last_name', 'password')


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Catalog


class BrendsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Brends


class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Collections


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Collections

class SocketCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Collections

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Product

class ProductBaskerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("article", "name", "price", "amount_for_basket")
        model = Product

class UserSerializer(serializers.ModelSerializer):
    user_products =ProductBaskerSerializer(many=True)

    class Meta:
        fields = ("email", "first_name", "last_name","user_products")
        model = User


class BasketSerializer(serializers.ModelSerializer):
    products_to_basket = ProductBaskerSerializer(many=True)
    class Meta:
        fields = "__all__"
        model = Basket

