from rest_framework import serializers

from apis.models import Todo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
