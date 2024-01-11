from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.views import TodoViewSet

router = SimpleRouter()

router.register("todo", TodoViewSet)


urlpatterns = [
    path("", include("users.urls")),
] + router.urls
