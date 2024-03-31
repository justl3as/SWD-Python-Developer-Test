from rest_framework import serializers


class ScoreCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=50)
    last_name = serializers.CharField(required=True, max_length=50)
    subject_title = serializers.CharField(required=True, max_length=50)
    score = serializers.IntegerField(required=True, min_value=0, max_value=100)
