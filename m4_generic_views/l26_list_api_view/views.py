from rest_framework.generics import ListAPIView
from .serializers import ProjectM4ReadSerializer
from .models import ProjectM4

class ProjectL26ListAPIView(ListAPIView):

    serializer_class = ProjectM4ReadSerializer
    queryset = ProjectM4.objects.all()

    