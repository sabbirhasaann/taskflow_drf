from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.serializers.task_own_serializer import TaskOwnSerializer
from django.core.exceptions import ValidationError


class TaskOwnAPIView(APIView):

    def post(self, request):

        serializer = TaskOwnSerializer(
            data=request.data,
            context={
                "request": request
            }
        )

        serializer.is_valid(raise_exception=True)

        if not request.user.is_authenticated:
            return Response(
                {
                    'detials': 'Authentication details were not provided.'
                }
            )
        task = serializer.save()

        return Response(
            TaskOwnSerializer(task).data,
            status=status.HTTP_201_CREATED
        )


# {
#     "title": "Title 1",
#     "description": "Description 1",
#     "project": 1
# }
