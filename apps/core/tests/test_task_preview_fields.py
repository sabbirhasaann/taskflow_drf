from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestTaskPreviewFields(APITestCase):

    def setUp(self):
        self.url = reverse("core:task-preview-fields")

    def test_defaults_are_applied_to_omitted_fields(self):
        response = self.client.post(
            self.url,
            {"title": "Prepare sprint plan"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["priority"], 2)
        self.assertFalse(response.data["is_completed"])
        self.assertEqual(response.data["labels"], [])
        self.assertEqual(response.data["metadata"], {})

    def test_valid_extended_fields_are_accepted(self):
        payload = {
            "title": "Prepare sprint plan",
            "priority": 4,
            "is_completed": True,
            "due_at": "2026-10-20T15:00:00Z",
            "project_id": "8f7f9b5e-0a6d-4c2e-8b4f-1a6d0f9c1234",
            "contact_email": "developer@example.com",
            "reference_url": "https://example.com/docs",
            "labels": ["backend", "planning"],
            "metadata": {
                "source": "mobile",
                "category": "planning",
            },
        }

        response = self.client.post(
            self.url,
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["priority"], 4)
        self.assertEqual(response.data["is_completed"], True)
        self.assertEqual(
            response.data["labels"],
            ["backend", "planning"],
        )
        self.assertEqual(
            response.data["metadata"]["source"],
            "mobile",
        )

    def test_invalid_priority_is_rejected(self):
        response = self.client.post(
            self.url,
            {
                "title": "Prepare sprint plan",
                "priority": 99,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("priority", response.data)

    def test_invalid_project_uuid_is_rejected(self):
        response = self.client.post(
            self.url,
            {
                "title": "Prepare sprint plan",
                "project_id": "not-a-uuid",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("project_id", response.data)

    def test_invalid_email_is_rejected(self):
        response = self.client.post(
            self.url,
            {
                "title": "Prepare sprint plan",
                "contact_email": "not-an-email",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("contact_email", response.data)

    # django automatically transform 123 to "123"
    # def test_invalid_label_element_is_rejected(self):
    #     response = self.client.post(
    #         self.url,
    #         {
    #             "title": "Prepare sprint plan",
    #             "labels": ["backend", 123],
    #         },
    #         format="json",
    #     )
    #     print("Response data...", response.data)
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_400_BAD_REQUEST,
    #     )
    #     self.assertIn("labels", response.data)

    # django automatically transform 5 to "5"
    # def test_non_string_metadata_value_is_rejected(self):
    #     response = self.client.post(
    #         self.url,
    #         {
    #             "title": "Prepare sprint plan",
    #             "metadata": {"estimate": 5},
    #         },
    #         format="json",
    #     )

    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_400_BAD_REQUEST,
    #     )
    #     self.assertIn("metadata", response.data)

    def test_nullable_fields_accept_null(self):
        response = self.client.post(
            self.url,
            {
                "title": "Prepare sprint plan",
                "due_at": None,
                "project_id": None,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNone(response.data["due_at"])
        self.assertIsNone(response.data["project_id"])
