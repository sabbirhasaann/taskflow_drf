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


class RequestDemoAPITests(APITestCase):
    def test_get_reads_query_parameters(self):
        response = self.client.get(
            reverse("core:request-demo"),
            {"status": "todo", "page": "2"},
            HTTP_ACCEPT="application/json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.data["query_params"],
            {"status": ["todo"], "page": ["2"]},
        )
        self.assertEqual(
            response.data["accepted_media_type"],
            "application/json",
        )

    def test_post_parses_json_request_body(self):
        payload = {
            "title": "Implement login",
            "status": "todo",
        }

        response = self.client.post(
            reverse("core:request-demo"),
            data=payload,
            format="json",
            HTTP_ACCEPT="application/json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.data["received_data"],
            payload,
        )
        self.assertEqual(
            response.data["content_type"],
            "application/json",
        )

    def test_post_rejects_unsupported_content_type(self):
        response = self.client.post(
            reverse("core:request-demo"),
            data="not-json",
            content_type="text/plain",
            HTTP_ACCEPT="application/json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        )