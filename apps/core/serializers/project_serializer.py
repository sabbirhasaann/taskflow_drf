from apps.core.models import Project
from rest_framework import serializers


class ProjectReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'status',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]


class ProjectWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project

        fields = [
            'name',
            'description',
            'status'
        ]
