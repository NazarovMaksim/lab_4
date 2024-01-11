from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.models import Todo
from app.serializers import TodoSerializer
from users.models import User
from users.serializers import DetailedUserSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.prefetch_related("todos")
    serializer_class = DetailedUserSerializer

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        return Response(status=200, data=UserSerializer(qs, many=True).data)

    @action(detail=True, methods=["get"])
    def todo(self, *args, **kwargs):
        user = self.get_object()
        return Response(
            data=TodoSerializer(Todo.objects.filter(user=user), many=True).data
        )

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if user.todos.exists():
            raise ValidationError("Can't delete user with existing todos")

        user.delete()
        return Response(status=204)
