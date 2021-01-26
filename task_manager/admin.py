from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'created', 'created_by')
    list_display = ('title', 'text', 'created', 'created_by')
    list_filter = ('created', 'created_by')
    search_fields = ('title', 'text')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'created_by')
