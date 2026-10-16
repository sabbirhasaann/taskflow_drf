from django.db import models


class TaskL23(models.Model):

    title = models.CharField(max_length=100)
    priority = models.IntegerField(default=2)
    is_completed = models.BooleanField(default=False)
