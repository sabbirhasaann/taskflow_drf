from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthCheckAPITests(APITestCase):

    def test_health_check_returns_expected_payload(self):
        url = reverse("core:health")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.data,
            {
                "status": "ok",
                "service": "taskflow-api",
                "api_version": "v1",
            },
        )

    def test_health_check_rejects_post(self):

        url = reverse("core:health")
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
