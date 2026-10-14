from rest_framework import serializers


class TaskPreviewSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=200)
    description = serializers.CharField(
        required=False,
        allow_blank=True,
    )
    is_completed = serializers.BooleanField(default=False)
