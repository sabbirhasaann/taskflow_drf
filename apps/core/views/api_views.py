from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.core.serializers.task_status_preview_serializer import TaskPreviewSerializer


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


class RequestDemoView(APIView):
    """
    Temporary development endpoint for learning DRF requests.
    Remove before production deployment.
    """

    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {
                "method": request.method,
                "query_params": dict(request.query_params),
                "content_type": request.headers.get("Content-Type"),
                "accept": request.headers.get("Accept"),
                "accepted_media_type": request.accepted_media_type,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        return Response(
            {
                "method": request.method,
                "received_data": request.data,
                "content_type": request.headers.get("Content-Type"),
                "accepted_media_type": request.accepted_media_type,
            },
            status=status.HTTP_200_OK,
        )


TASK_STATUS_TRANSITIONS = {
    "todo": {
        "in_progress"
    },
    "in_progress": {
        "completed"
    },
    "completed": set(),
}


class TaskListCreateView(APIView):

    def post(self, request):
        data = request.data

        if not isinstance(data, dict):
            return Response(
                {
                    "detail": "The request body must be a JSON object."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        current_status = data.get("current_status")
        new_status = data.get("new_status")

        valid_statuses = set(TASK_STATUS_TRANSITIONS.keys())

        if (not isinstance(current_status, str) or current_status not in valid_statuses):
            return Response(
                {
                    "current_status": [
                        "Provide a valid task status"
                    ]
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if (not isinstance(new_status, str) or new_status not in valid_statuses):
            return Response(
                {
                    "new_status": [
                        "Provide a valid task status"
                    ]
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        allowed = (new_status in TASK_STATUS_TRANSITIONS[current_status])

        return Response(
            {
                "allowed": allowed,
                "current_status": current_status,
                "new_status": new_status,
            },
            status=status.HTTP_200_OK,
        )


class TaskPreviewView(APIView):

    def post(self, request):

        serializer = TaskPreviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
