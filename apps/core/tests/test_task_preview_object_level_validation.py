from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestTaskPreviewObjectLevelValidation(APITestCase):

    def setUp(self):
        self.url = reverse("core:task-preview-object-level-validation-view")
        print("Test Executing....0")

    def test_deadline_before_start_time_is_rejected(self):
        payload = {
            "title": "Prepare sprint release",
            "starts_at": "2026-10-20T15:00:00Z",
            "due_at": "2026-10-19T15:00:00Z",
        }
        response = self.client.post(
            self.url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.assertIn("due_at", response.data)
        print("Test Executing....1")

    def test_deadline_equal_to_start_time_is_accepted(self):

        payload = {
            "title": "Prepare sprint release",
            "starts_at": "2026-10-20T15:00:00Z",
            "due_at": "2026-10-20T15:00:00Z",
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
        print("Test Executing....2")

    def test_deadline_after_start_time_is_accepted(self):
        payload = {
            "title": "Prepare sprint release",
            "starts_at": "2026-10-20T15:00:00Z",
            "due_at": "2026-10-21T15:00:00Z",
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
        print("Test Executing....3")

    def test_deadline_without_start_time_is_accepted(self):

        payload = {
            "title": "Prepare sprint release",
            "due_at": "2026-10-21T15:00:00Z",
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
        print("Test Executing....4")

    def test_null_start_and_deadline_are_accepted(self):
        payload = {
            "title": "Prepare sprint release",
            "starts_at": None,
            "due_at": None,
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

        self.assertIsNone(response.data["starts_at"])
        self.assertIsNone(response.data["due_at"])
        print("Test Executing....5")
