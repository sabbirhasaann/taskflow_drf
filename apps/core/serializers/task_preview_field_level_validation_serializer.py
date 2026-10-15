from rest_framework import serializers


class TaskPreviewFieldLevelValidataionSerializer(serializers.Serializer):

    title = serializers.CharField(
        max_length=200,
        trim_whitespace=True,
    )

    labels = serializers.ListField(
        child=serializers.CharField(
            max_length=40,
            trim_whitespace=True,
        ),
        required=False,
        default=list,
        allow_empty=True,
    )

    reference_url = serializers.URLField(
        required=False,
        allow_blank=True,
    )

    def validate_title(self, value):
        """Require at least one letter or digit in the title."""
        if not any(character.isalnum() for character in value):
            raise serializers.ValidationError(
                "The title must contain at least one letter or digit."
            )
        return value

    def validate_labels(self, value):
        """Reject duplicate labels, ignoring case."""
        normalized_labels = [
            label.casefold()
            for label in value
        ]
        if len(normalized_labels) != len(set(normalized_labels)):
            raise serializers.ValidationError(
                "Labels must not contain duplicates."
            )
        return value

    def validate_reference_url(self, value):
        """Require HTTPS for external reference URLs."""
        if value and not value.lower().startswith("https://"):
            raise serializers.ValidationError(
                "Reference URLs must use HTTPS."
            )
        return value

