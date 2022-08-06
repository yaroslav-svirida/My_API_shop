from django.urls import reverse
from rest_framework.test import APITestCase

class BooksApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('products-list')
        print(url)
        response = self.client.get(url)
        print(response)

    def test_get_video(self):
        muffin = User.objects.get(first_name="Muffin")
        muffin.unbann_user()
        self.assertEqual(muffin.is_banned, False)