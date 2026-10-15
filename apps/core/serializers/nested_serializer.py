from rest_framework import serializers
from apps.core.models import ProjectRel,TaskRel

class ProjectSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRel
        fields=['id', 'title']


class TaskReadSerializer(serializers.ModelSerializer):

    project = ProjectSummarySerializer(read_only=True)

    class Meta:
        model=TaskRel
        fields=['id', 'title', 'project']
        read_only_fields=['id']
