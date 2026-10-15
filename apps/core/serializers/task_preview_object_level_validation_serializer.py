from rest_framework import serializers


class TaskPreviewObjectLevelValidationSerializer(serializers.Serializer):

    """
    Validate and represent task-preview input.

    This serializer does not persist a Task model.
    """

    title = serializers.CharField(
        max_length=200,
        trim_whitespace=True,
    )
    description = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=2000,
    )
    priority = serializers.ChoiceField(
        choices=[
            (1, "Low"),
            (2, "Normal"),
            (3, "High"),
            (4, "Urgent"),
        ],
        default=2,
    )
    is_completed = serializers.BooleanField(
        required=False,
        default=False,
    )
    starts_at = serializers.DateTimeField(
        required=False,
        allow_null=True,
    )
    due_at = serializers.DateTimeField(
        required=False,
        allow_null=True,
    )
    project_id = serializers.UUIDField(
        required=False,
        allow_null=True,
    )
    contact_email = serializers.EmailField(
        required=False,
        allow_blank=True,
    )
    reference_url = serializers.URLField(
        required=False,
        allow_blank=True,
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
    metadata = serializers.DictField(
        child=serializers.CharField(max_length=100),
        required=False,
        default=dict,
    )

    def validate_title(self, value):
        """Require at least one letter or digit."""
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
        """Require HTTPS for reference URLs."""
        if value and not value.lower().startswith("https://"):
            raise serializers.ValidationError(
                "Reference URLs must use HTTPS."
            )
        return value

    def validate(self, attrs):
        """
        Validate rules involving multiple fields.
        """
        starts_at = attrs.get("starts_at")
        due_at = attrs.get("due_at")

        if (
            starts_at is not None
            and due_at is not None
            and due_at < starts_at
        ):
            raise serializers.ValidationError({
                "due_at": (
                    "The deadline must be equal to or later "
                    "than the task start time."
                )
            })

        return attrs
