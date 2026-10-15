from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestTaskPreviewFieldLevelValidation1(APITestCase):

    def setUp(self):
        self.url = reverse("core:task-preview-field-level-validation")
        print("Test Executing....")

    def test_title_containing_only_punctuation_is_rejected(self):
        response = self.client.post(
            self.url,
            {"title": "!!!"},
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("title", response.data)
        print("Test Executing....1")

    def test_title_containing_letters_and_punctuation_is_accepted(self):
        response = self.client.post(
            self.url,
            {"title": "Sprint #3!"},
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        print("Test Executing....2")

    def test_duplicate_labels_are_rejected_case_insensitively(self):
        response = self.client.post(
            self.url,
            {
                "title": "Prepare sprint plan",
                "labels": ["Backend", "backend"],
            },
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("labels", response.data)
        print("Test Executing....3")

    def test_distinct_labels_are_accepted(self):
        response = self.client.post(
            self.url,
            {
                "title": "Prepare sprint plan",
                "labels": ["Backend", "Frontend"],
            },
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.data["labels"],
            ["Backend", "Frontend"],
        )
        print("Test Executing....4")

    def test_http_reference_url_is_rejected(self):
        response = self.client.post(
            self.url,
            {
                "title": "Review API documentation",
                "reference_url": "http://example.com/docs",
            },
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )
        self.assertIn("reference_url", response.data)
        print("Test Executing....5")

    def test_https_reference_url_is_accepted(self):
        response = self.client.post(
            self.url,
            {
                "title": "Review API documentation",
                "reference_url": "https://example.com/docs",
            },
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        print("Test Executing....6")
