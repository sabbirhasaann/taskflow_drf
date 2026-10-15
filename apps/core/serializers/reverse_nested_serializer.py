from rest_framework import serializers
from apps.core.models import ProjectRel, TaskRel


class TaskSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskRel
        fields = ['id', 'title', 'project']
        read_only_fields = ['id']


class ProjectDetailSerializer(serializers.ModelSerializer):
    tasks = TaskSummarySerializer(many=True, read_only=True)

    class Meta:
        model = ProjectRel
        fields = ['id', 'title', 'tasks']
