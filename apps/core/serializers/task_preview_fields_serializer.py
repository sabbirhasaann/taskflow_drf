from rest_framework import serializers


class TaskPreviewFieldsSerializer(serializers.Serializer):
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
        child=serializers.CharField(
            max_length=100,
        ),
        required=False,
        default=dict,
    )
