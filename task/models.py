from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class TodoList(models.Model):
    todo_list = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class meta:
        ordering = ["complete"]


class Task(models.Model):
    todo_list = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
