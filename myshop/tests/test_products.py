from django.test import TestCase, Client
import json

from rest_framework import status

from myshop.models import Product, User
from myshop.serializers import  ProductSerializer


client = Client()


class ProductTest(TestCase):

    def setUp(self) -> None:
        self.valid_payload = {
            "name": "TestName",
            "article": "TestArticle"

        }
        self.brand = Product.objects.create(name="SE",
                                            article="TEST"
                                            )
        self.user = User.objects.create(email='test_user@mail.ru',
                                        first_name='test_user',
                                        password='test_password123'
                                        )

    def test_get_products(self):
        response = client.get("/product/get/")
        product = Product.objects.all()
        serializer_product = ProductSerializer(product, many=True).data
        self.assertEqual(response.data, serializer_product)

    def test_create_product(self):
        response = client.post("/product/create/",
                               json.dumps(self.valid_payload),
                               content_type='application/json'
                               )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        create_product = Product.objects.get(id=response.data.get("id"))
        serialized_product = ProductSerializer(create_product).data
        self.assertEqual(response.data, serialized_product)

    def test_product_fail(self):
        response = client.get("/product/get/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_product(self):
        response = client.get("/product/get/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        url = 'http://127.0.0.1:8000/product/delete/1/'
        client.force_login(self.user)
        response = client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_update(self):
        url = 'http://127.0.0.1:8000/product/update/1/'
        data = {
            "name": "Legrand"

        }
        json_data = json.dumps(data)

        response = client.put(url, data=json_data,
                              content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
