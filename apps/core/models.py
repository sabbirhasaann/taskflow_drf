from django.db import models
from django.conf import settings


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


class ProjectOwn(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TaskOwn(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    project = models.ForeignKey(
        ProjectOwn,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.IntegerField(default=2)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LabelMany(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class TaskMany(models.Model):
    title = models.CharField(max_length=200)
    labels = models.ManyToManyField(
        LabelMany,
        related_name='tasksmany',
        blank=True
    )

    def __str__(self):
        return self.title
