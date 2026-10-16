from .models import TaskL23
from rest_framework import serializers


class TaskL23Serializer(serializers.ModelSerializer):

    priority_label = serializers.SerializerMethodField()

    class Meta:
        model = TaskL23
        fields = [
            'id',
            'title',
            'priority',
            'priority_label',
            'is_completed',
        ]

        read_only_fields = [
            'id',
            'priority_label'
        ]

    def get_priority_label(self, obj):

        labels = {
            1: 'Low',
            2: 'Normal',
            3: 'High',
            4: 'Urgent'
        }

        return labels.get(obj.priority, "Unknown")

    def create(self, validated_data):

        print("Validated data...", validated_data)

        return TaskL23.objects.create(**validated_data)
