from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import TaskL23
from .serializers import TaskL23Serializer


class TaskL23CreateView(APIView):

    def post(self, request):

        serializer = TaskL23Serializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        taskl23 = serializer.save()

        return Response(
            TaskL23Serializer(taskl23).data,
            status=status.HTTP_201_CREATED
        )


# {
#     "title": "Title 1",
#     "priority": 4
# }