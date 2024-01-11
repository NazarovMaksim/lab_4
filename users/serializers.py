from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from app.serializers import TodoSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class DetailedUserSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "todos",
        ]
