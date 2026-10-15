from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.PositiveSmallIntegerField(default=2)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProjectRel(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class TaskRel(models.Model):
    project = models.ForeignKey(
        ProjectRel,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
