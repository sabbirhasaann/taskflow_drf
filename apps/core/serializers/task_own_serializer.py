from rest_framework import serializers
from apps.core.models import TaskOwn, ProjectOwn


class TaskOwnSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskOwn
        fields = [
            'id',
            'project',
            'title',
            'description',
            'priority',
            'is_completed',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'owner',
            'created_at',
            'updated_at'
        ]

    def validate_project(self, value):
        """Checks if the project belongs to the requesting user."""

        request = self.context.get('request')
        user = request.user if request else None

        if not ProjectOwn.objects.filter(pk=value.pk, owner=user).exists():
            raise serializers.ValidationError(
                "This project does not exist or you do not have permission to use it."
            )
        return value

    def create(self, validated_data):

        request = self.context.get('request')
        user = request.user if request else None

        if not user or not user.is_authenticated:
            raise serializers.ValidationError(
                {
                    "detail": "Authentication credentials were not provided."
                }
            )

        print("Task successfully created for... ", user)
        return TaskOwn.objects.create(owner=user, **validated_data)
