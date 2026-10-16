from rest_framework import serializers
from apps.core.models import ProjectOwn


class ProjectOwnSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectOwn
        fields = [
            'id',
            'owner',
            'name',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'owner',
            'created_at',
            'updated_at'
        ]

# {
#     "name": "Project Own 1"
# }
