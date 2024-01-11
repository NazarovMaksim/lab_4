from rest_framework.viewsets import ModelViewSet

from app.models import Todo
from app.serializers import TodoWithUserSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoWithUserSerializer
