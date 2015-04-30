from django.contrib import admin
from ellipse.models import Task

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['taskname']}),
        (None, {'fields': ['added_on']}),
        (None, {'fields': ['deadline']}),
        (None, {'fields': ['completed']}),
    ]
    list_display = ('taskname', 'deadline')

admin.site.register(Task, TaskAdmin)


