from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.serializers.nested_serializer import TaskReadSerializer
from apps.core.models import TaskRel


class NestedSerializerView(APIView):

    def get(self, request, id):

        task = TaskRel.objects.get(pk=id)

        return Response(
            TaskReadSerializer(task).data,
            status=status.HTTP_200_OK
        )
