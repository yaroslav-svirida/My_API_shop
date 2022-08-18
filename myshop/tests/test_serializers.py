from django.test import TestCase

from myshop.models import Brends
from myshop.serializers import BrendsSerializer


class BrandSerializerTestCase(TestCase):
    def test_ok(self):
        brand_1 = Brends.objects.create(name='ABB')
        brand_2 = Brends.objects.create(name='SE')
        data = BrendsSerializer([brand_1, brand_2], many=True).data
        expected_data = [

            {'id': brand_1.id,
             'name': 'ABB'},

            {'id': brand_2.id,
             'name': 'SE'},

        ]
        self.assertEqual(expected_data, data)
