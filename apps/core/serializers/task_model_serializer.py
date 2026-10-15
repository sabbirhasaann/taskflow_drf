from rest_framework import serializers

from apps.core.models import Task


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "is_completed",
        ]
        read_only_fields = ["id"]
