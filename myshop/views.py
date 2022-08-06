from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import CatalogSerializer, BrendsSerializer, CollectionsSerializer, ColorsSerializer, \
    SocketCategoriesSerializer, ProductSerializer, BasketSerializer


class CatalogView(APIView):

    def post(self, request):
        name = request.data.get('name')
        name = Catalog.objects.create(name=name)
        name_serialized = CatalogSerializer(name).data
        return Response(name_serialized)

    def get(self, request, pk=None):
        try:
            if not pk:
                all = Catalog.objects.all()
                all_serialezed = CatalogSerializer(all, many=True).data
                return Response(all_serialezed)
            all = Catalog.objects.filter(id=pk)
            all_serialezed = CatalogSerializer(all).data
            return Response(all_serialezed)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        catalog = Catalog.objects.get(id=pk)
        serializer = CatalogSerializer(catalog, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk):
    #     Catalog.objects.filter(id=pk).update(**request.data)
    #     catalog = Catalog.objects.get(id=pk)
    #     serializer_catalog = CatalogSerializer(catalog).data
    #     return Response(serializer_catalog)
    #

    # catalog = Catalog.objects.get(id=pk)
    # name_old = catalog.name
    # name_new = request.data('name')
    # name.objects.update(name_old = name_new)
    # serializer = CatalogSerializer(name)
    #
    #
    # serializer.save()
    # return Response(serializer.data)
    # # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            com = Catalog.objects.get(pk=pk)

        except Catalog.DoesNotExist:
            raise Http404
        com.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrendsView(APIView):

    def post(self, request):
        name = request.data.get('name')
        brend = Brends.objects.create(name=name)
        name_serialized = BrendsSerializer(brend).data
        return Response(name_serialized)

    def get(self, request, pk=None):
        try:
            if not pk:
                all = Brends.objects.all()
                all_serialezed = BrendsSerializer(all, many=True).data
                return Response(all_serialezed)
            all = Brends.objects.filter(id=pk)
            all_serialezed = BrendsSerializer(all).data
            return Response(all_serialezed)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        brend = Brends.objects.get(id=pk)
        serializer = BrendsSerializer(brend, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            brend = Brends.objects.get(id=pk)

        except Brends.DoesNotExist:
            raise Http404
        brend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionsView(APIView):

    def post(self, request):
        name = request.data.get('name')
        collection = Collections.objects.create(name=name)
        name_serialized = CollectionsSerializer(collection).data
        return Response(name_serialized)

    def get(self, request, pk=None):
        try:
            if not pk:
                all = Collections.objects.all()
                all_serialezed = CollectionsSerializer(all, many=True).data
                return Response(all_serialezed)
            all = Collections.objects.filter(id=pk)
            all_serialezed = CollectionsSerializer(all).data
            return Response(all_serialezed)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        collection = Collections.objects.get(id=pk)
        serializer = CollectionsSerializer(collection, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            collection = Collections.objects.get(pk=pk)

        except Brends.DoesNotExist:
            raise Http404
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ColorsView(APIView):
    def post(self, request):

        color = request.data.get("name")
        create_color = Colors.objects.create(name=color)
        color_serialized = ColorsSerializer(create_color).data
        return Response(color_serialized)

    def get(self, request, pk=None):
        try:
            if not pk:
                color = Colors.objects.all()
                color_serialized = ColorsSerializer(color).data
                return Response(color_serialized)
            color = Colors.objects.get(id=pk)
            color_serialized = ColorsSerializer(color).data
            return Response(color_serialized)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        color = Colors.objects.get(id=pk)
        serializer = ColorsSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            color = Colors.objects.get(id=pk)
        except Colors.DoesNotExist:
            raise Http404
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SocketsCategoryView(APIView):
    def post(self, request):
        name = request.data.get("name")
        socketCategory = SocketsCategory.objects.create(name=name)
        socketCategory_serialized = SocketCategoriesSerializer(socketCategory).data
        return Response(socketCategory_serialized)

    def get(self, request, pk=None):
        try:
            if not pk:
                category = SocketsCategory.objects.all()
                category_serialized = SocketCategoriesSerializer(category, many=True).data
                return Response(category_serialized)
            category = SocketsCategory.objects.get(id=pk)
            category_serialized = SocketCategoriesSerializer(category).data
            return Response(category_serialized)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        socketCategory = SocketsCategory.objects.get(id=pk)
        serializer = SocketCategoriesSerializer(socketCategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = SocketsCategory.objects.get(id=pk)
        except SocketsCategory.DoesNotExist:
            raise Http404
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductView(APIView):

    def post(self, request):
        name = request.data.get("name")
        product = Product.objects.create(name=name)
        product_serialized = ProductSerializer(product).data
        return Response(product_serialized)

    def get(self, request, pk=None):
        try:
            if not pk:
                product = Product.objects.all()
                product_serialized = ProductSerializer(product, many=True).data
                return Response(product_serialized)
            product = Product.objects.get(id=pk)
            product_serialized = ProductSerializer(product).data
            return Response(product_serialized)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except SocketsCategory.DoesNotExist:
            raise Http404
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BasketView(APIView):
    def post(self, request):
        id = request.data.get("id")
        basket = Basket.objects.get(id=6)
        product = Product.objects.get(id=id)
        # product.amount_for_basket = request.data.get("amount_for_basket")
        # product.save()
        basket.products_to_basket.add(product)
        basket.save()
        user_basket_serialized = BasketSerializer(basket).data
        return Response(user_basket_serialized)

    def get(self, request):
        basket = Basket.objects.get(id=6)
        product_serialized = BasketSerializer(basket).data
        return Response(product_serialized)

    def delete(self, request, pk):
        try:
            basket = Basket.objects.get(pk=pk)
        except Basket.DoesNotExist:
            raise Http404
        basket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
