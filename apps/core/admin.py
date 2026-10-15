from django.contrib import admin
from .models import Task, TaskRel, ProjectRel
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskRel)
admin.site.register(ProjectRel)
