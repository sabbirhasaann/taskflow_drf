from rest_framework import serializers

from apps.core.models import TaskRel, ProjectRel


class TaskRelSerializer(serializers.ModelSerializer):

    project = serializers.PrimaryKeyRelatedField(
        queryset=ProjectRel.objects.all()
    )

    class Meta:
        model = TaskRel
        fields = [
            'id',
            'project',
            'title',
        ]

        read_only_fields = [
            'id'
        ]


class ProjectRelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectRel

        fields = [
            'id',
            'title'
        ]
