from django.test import TestCase, Client
import json
# Create your tests here.
from django.urls import reverse
from rest_framework import status

from myshop.models import Product, Brends, User
from myshop.serializers import BrendsSerializer, ProductSerializer
from rest_framework.test import APITestCase, APIClient

client = Client()


class Check(TestCase):


    def test_get_products(self):
        response = client.get("/product/get/")
        product = Product.objects.all()
        serializer_product = ProductSerializer(product, many=True).data
        self.assertEqual(response.data, serializer_product)


class GetPostBrandTest(TestCase):

    def setUp(self) -> None:
        self.valid_payload = {
            "name": "TestBrand",

        }
        self.brand = Brends.objects.create(name='SE')
        self.user = User.objects.create(email='test_user@mail.ru', first_name='test_user',
                                   password='test_password123')
        self.brends = Brends.objects.all()


    def test_get_brands(self):
        response = client.get("/brend/get/")

        serializer_brand = BrendsSerializer(self.brends, many=True).data
        self.assertEqual(response.data, serializer_brand)

    def test_create_video(self):
        response = client.post("/brend/create/", json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        video_object = Brends.objects.get(id=response.data.get("id"))
        serialized_video = BrendsSerializer(video_object).data
        self.assertEqual(response.data, serialized_video)

    def test_brand_fail(self):
        response = client.get("/brend/get/10/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_brand(self):
        print(self.brand.id)
        response = client.get("/brend/get/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_delete(self):

        url = 'http://127.0.0.1:8000/brend/delete/1/'
        client.force_login(self.user)
        response = client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_update(self):

        url = 'http://127.0.0.1:8000/brend/update/1/'
        data = {
            "name": "Legrand"

        }
        json_data = json.dumps(data)

        response = client.put(url, data=json_data,
                              content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
