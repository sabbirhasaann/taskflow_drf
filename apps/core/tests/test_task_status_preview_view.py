from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestTaskStatusPreview(APITestCase):

    def setUp(self):
        self.url = reverse("core:v2-task-status-preview")

    def test_put_method_is_not_allowed(self):

        response = self.client.put(
            self.url,
            {
                "current_status": "todo",
                "new_status": "in_progress",
            },
            format="json",
        )

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
