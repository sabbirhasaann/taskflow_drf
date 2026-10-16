from rest_framework import serializers
from apps.core.models import TaskOwn


class ProjectOwnSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskOwn
        fields = [
            'id',
            'owner',
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
            'created_at',
            'updated_at'
        ]
