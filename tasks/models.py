from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "To Do"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"

    title = models.CharField(
        max_length=255,
        verbose_name="Title"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
        verbose_name="Status"
    )

    deadline = models.DateField(
        verbose_name="Deadline"
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Owner"
    )

    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Created at"
    )

    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Updated at"
    )

    def __str__(self):
        return f"{self.title} ({self.owner.username})"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
