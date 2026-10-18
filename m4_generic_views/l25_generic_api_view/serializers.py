from rest_framework import serializers
from .models import ProjectL25


class ProjectL25Serializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectL25
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


class ProjectL25WriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectL25

        fields = [
            'name',
            'description',
            'status',
        ]
