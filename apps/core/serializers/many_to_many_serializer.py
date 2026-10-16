from rest_framework import serializers
from apps.core.models import LabelMany, TaskMany


class LabelManySerializer(serializers.ModelSerializer):

    class Meta:
        model = LabelMany
        fields = ['id', 'label']
        read_only_fields = ['id']


class TaskManySerializer(serializers.ModelSerializer):

    labels = LabelManySerializer(many=True, read_only=True)
    label_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=LabelMany.objects.all(),
        write_only=True,
        source="labels",
        required=False,
    )

    class Meta:
        model = TaskMany
        fields = ['id', 'title', 'labels', 'label_ids']
        read_only_fields = ['id']
