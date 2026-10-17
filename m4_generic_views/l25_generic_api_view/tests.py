from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import ProjectL25
from rest_framework import status

# python manage.py test m4_generic_views/l25_generic_api_view
# python manage.py test m4_generic_views.l25_generic_api_view



class TestProjectL25ListAPIView(APITestCase):

    def setUp(self):
        self.url = reverse('l25:list-projectsl25')

    def test_list_projects_return_200(self):

        response = self.client.get(
            self.url
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_post_is_not_supported(self):

        response = self.client.post(
            self.url,
            {},
            format='json'
        )

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
