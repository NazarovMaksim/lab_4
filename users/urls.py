from django.urls import path
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet

router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [path("/", UserViewSet.as_view({"get": "todo"}))] + router.urls
