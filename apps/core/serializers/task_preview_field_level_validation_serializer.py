from rest_framework import serializers


class TaskPreviewFieldLevelValidataionSerializer(serializers.Serializer):

    title = serializers.CharField(
        max_length=200,
        trim_whitespace=True,
    )

    def validate_title(self, value):
        if "!" in value:
            raise serializers.ValidationError(
                "Titles must not contain exclamation marks."
            )
        return value
