from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="todos"
    )
