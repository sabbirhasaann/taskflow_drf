from rest_framework import serializers


class TaskPreviewSerializer(serializers.Serializer):

    title = serializers.CharField(
    max_length=200,
    trim_whitespace=True,
    )
    description = serializers.CharField(        
        required=False,        
        allow_blank=True,        
        max_length=2000,    
    )    
    
    is_completed = serializers.BooleanField(        
        required=False,        
        default=False,    
    )
