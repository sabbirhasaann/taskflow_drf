from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TaskStatusPreviewAPITests(APITestCase):

    def setUp(self):
        self.url = reverse('core:task-status-preview')

    def test_allowed_transition_returns_true(self):
        payload = {
            "current_status": "todo",
            "new_status": "in_progress",
        }

        response = self.client.post(self.url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {
                "allowed": True,
                "current_status": "todo",
                "new_status": "in_progress",
            }
        )

    def test_disallowed_transition_returns_false(self):
        response = self.client.post(
            self.url,
            {
                "current_status": "todo",
                "new_status": "completed",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["allowed"])

    def test_invalid_status_returns_400(self):
        response = self.client.post(
            self.url,
            {
                "current_status": "unknown",
                "new_status": "completed",
            },
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("current_status", response.data)

    # def test_non_string_status_returns_400(self):
    #     response = self.client.post(
    #         self.url,
    #         {
    #             "current_status": ["todo"],
    #             "new_status": "in_progress",
    #         },
    #         format="json",
    #     )
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_400_BAD_REQUEST,
    #     )

    def test_get_is_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED,
        )
