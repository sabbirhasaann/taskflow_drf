from rest_framework.views import APIView
from rest_framework.response import Response
from apps.core.serializers.task_model_serializer import TaskModelSerializer
from rest_framework import status
from apps.core.models import Task


class TaskModelSerializerView(APIView):

    def post(self, request):

        t = Task.objects.get(id=1)

        serializer = TaskModelSerializer(
            data=request.data
        )
        print(repr(serializer))
        serializer.is_valid(raise_exception=True)

        task = serializer.save()

        return Response(
            {
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "is_completed": task.is_completed
            },
            status=status.HTTP_200_OK
        )

    def put(self, request):

        id = request.data["id"]
        task = Task.objects.get(
            pk=id
        )

        serializer = TaskModelSerializer(
            instance=task,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        updated_task = serializer.save()

        return Response(
            TaskModelSerializer(updated_task).data,
            status=status.HTTP_200_OK,
        )


# {
#     "id": 1,
#     "title": "This is the udpated tile",
#     "description": "This is the updated description"
# }
