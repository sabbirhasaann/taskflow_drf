from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestCreateTaskAPIView(APITestCase):

    def setUp(self):
        self.url = reverse('core:create-task')

    def test_successful_creation(self):

        response = self.client.post(
            self.url,
            {
                "title": "Title 1",
                "description": "Description and..."
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Title 1")
