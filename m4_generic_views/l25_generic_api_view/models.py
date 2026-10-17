from django.db import models
from django.conf import settings


class ProjectL25(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        ON_HOLD = "on_hold", "On Hold"
        COMPLETED = "completed", "Completed"
        ARCHIVED = "archived", "Archived"

    # Core Fields
    name = models.CharField(max_length=255, unique=True)

    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
        db_index=True,
    )

    # Relations
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projectsl25",
    )

    # Audit Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
