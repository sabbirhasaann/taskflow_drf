from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.models import LabelMany, TaskMany
from apps.core.serializers.many_to_many_serializer import LabelManySerializer, TaskManySerializer
from django.shortcuts import get_object_or_404

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

    def post(self, request):

        serializer = LabelManySerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        label = serializer.save()

        return Response(
            LabelManySerializer(label).data,
            status=status.HTTP_201_CREATED
        )


class TaksManyDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(TaskMany, pk=pk)

    def get(self, request, id):

        taskmany = self.get_object(pk=id)

        return Response(
            TaskManySerializer(taskmany).data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskManySerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskManySerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LabelDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(LabelMany, pk=pk)

    def get(self, request, pk):
        label = self.get_object(pk)
        serializer = LabelManySerializer(label)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        label = self.get_object(pk)
        serializer = LabelManySerializer(label, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        label = self.get_object(pk)
        serializer = LabelManySerializer(
            label, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        label = self.get_object(pk)
        label.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
