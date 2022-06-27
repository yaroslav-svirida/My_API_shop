from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from myshop.serializers import ProductSerializer, UserSerializer


class BasketView(APIView):

    def post(self, request):
        product_id = request.data.get("id")
        product = Product.objects.get(id=product_id)
        user_basket = User.objects.get(id=request.user.id)
        user_basket.user_products.add(product)
        user_basket.save()
        user_basket_serialized = UserSerializer(user_basket).data
        return Response(user_basket_serialized)

    def get(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user_serialized = UserSerializer(user).data
        return Response(user_serialized)

    def delete(self, request):
        product_id = request.data.get("product_id")
        product = Product.objects.get(id=product_id)
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user.user_products.remove(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        product_id = request.data.get("product_id")
        product = Product.objects.get(id=product_id)
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user_product_for_update = user.user_products.get(product)


        serializer = UserSerializer(user_product_for_update, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)