from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created']
    search_fields = ['title', 'text']
    date_hierarchy = 'created'
    readonly_fields = ['title']
