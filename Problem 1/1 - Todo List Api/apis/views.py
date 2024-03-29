from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializers import ToDoSerializer


class ToDoListViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
