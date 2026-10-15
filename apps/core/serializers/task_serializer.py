from rest_framework import serializers
from apps.core.models import Task


class CreateTaskSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True)
    priority = serializers.IntegerField(default=2)
    is_completed = serializers.BooleanField(default=False)

    def validate_title(self, value):

        if '!' in value:
            raise serializers.ValidationError(
                {
                    'error': 'title must on contian !'
                }
            )
        return value

    def create(self, validate_data):
        return Task.objects.create(**validate_data)

    def update(self, instance, validate_data):

        instance.title = validate_data.get("title", instance.title),
        instance.description = validate_data.get(
            "description", instance.description)
        instance.priority = validate_data.get("priority", instance.priority)
        instance.is_completed = validate_data.get(
            "is_completed", instance.is_completed)

        instance.save()
        return instance

    # more resuable updated pattern
    # def update(self, instance, validated_data):
    #     for field, value in validated_data.items():
    #         setattr(instance, field, value)

    #         instance.save()
    #         return instance
