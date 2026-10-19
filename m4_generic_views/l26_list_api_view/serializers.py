from rest_framework import serializers
from .models import ProjectM4


class ProjectM4ReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectM4
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
            'owner',
            'created_at',
            'updated_at',
        ]


class ProjectM4WriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectM4

        fields = [
            'name',
            'description',
            'status',
        ]
