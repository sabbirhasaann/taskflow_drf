from rest_framework import serializers

from apps.core.models import Task


class TaskModelSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=200,
        trim_whitespace=True
    )

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

    def validate_title(self, value):
        if not any(character.isalnum() for character in value):
            raise serializers.ValidationError(
                "The title must contain at least one letter or digit."
            )
        return value
