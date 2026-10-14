from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TaskPreviewAPITests(APITestCase):
    def setUp(self):
        self.url = reverse("core:task-preview")

    def test_valid_task_input_returns_normalized_data(self):
        payload = {
            "title": "  Implement login screen  ",
            "description": "Build the responsive interface",
            "is_completed": False,
        }

        response = self.client.post(
            self.url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.data,
            {
                "title": "Implement login screen",
                "description": "Build the responsive interface",
                "is_completed": False,
            },
        )

    def test_omitted_optional_fields_use_expected_behavior(self):
        response = self.client.post(
            self.url,
            {"title": "Write serializer tests"},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.data,
            {
                "title": "Write serializer tests",
                "is_completed": False,
            },
        )

    def test_blank_title_is_rejected(self):
        response = self.client.post(
            self.url,
            {"title": "   "},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("title", response.data)

    def test_title_over_maximum_length_is_rejected(self):
        response = self.client.post(
            self.url,
            {"title": "x" * 201},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("title", response.data)

    def test_invalid_boolean_is_rejected(self):
        response = self.client.post(
            self.url,
            {
                "title": "Write tests",
                "is_completed": "not-a-boolean",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("is_completed", response.data)
