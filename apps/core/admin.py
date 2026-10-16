from django.contrib import admin
from .models import (
    Task,
    TaskRel,
    ProjectRel,
    ProjectOwn,
    TaskOwn,
)
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskRel)
admin.site.register(ProjectRel)
admin.site.register(ProjectOwn)
admin.site.register(TaskOwn)
