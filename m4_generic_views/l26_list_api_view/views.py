from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProjectM4ReadSerializer
from .models import ProjectM4


class ProjectL26ListAPIView(ListAPIView):

    serializer_class = ProjectM4ReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProjectM4.objects.filter(owner=self.request.user)
