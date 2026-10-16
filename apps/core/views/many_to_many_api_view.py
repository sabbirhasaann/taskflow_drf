from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.models import LabelMany, TaskMany
from apps.core.serializers.many_to_many_serializer import LabelManySerializer, TaskManySerializer


# ----------------------------------------------------
# 1. TASK ENDPOINTS (List & Create)
# ----------------------------------------------------
class TaskManyListCreateAPIView(APIView):
    def get(self, request):
        tasks = TaskMany.objects.all()
        serializer = TaskManySerializer(tasks, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = TaskManySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# {
#     "title": "Task Many Title 1"
# }


class LabelManyListCreateAPIView(APIView):

    def get(self, request):

        labels = LabelMany.objects.all()

        return Response(
            LabelManySerializer(labels, many=True).data,
            status=status.HTTP_200_OK
        )
    