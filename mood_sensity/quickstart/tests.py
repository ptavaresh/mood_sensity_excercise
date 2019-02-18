from django.test import TestCase

# Create your tests here.
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('picture/', include('mood_sensity.urls')),
    ]

    def test_create_account(self):
        """
        Ensure we can create a new picture object.
        """
        url = reverse('picture-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)