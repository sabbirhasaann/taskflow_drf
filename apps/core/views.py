from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """    Return basic liveness information for the TaskFlow API.    """

    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {
                "status": "ok",
                "service": "taskflow-api",
                "api_version": "v1",
            },
            status=status.HTTP_200_OK,
        )
