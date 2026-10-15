from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.serializers.reverse_nested_serializer import ProjectDetailSerializer
from apps.core.models import ProjectRel


class ReverseNestedSerializerView(APIView):

    def get(self, request, id):

        project = ProjectRel.objects.get(pk=id)

        return Response(
            ProjectDetailSerializer(project).data,
            status=status.HTTP_200_OK
        )
