from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'created', 'last_modified', 'created_by', 'is_active')
    list_display = ('title', 'text', 'created', 'last_modified', 'created_by', 'is_active')
    list_filter = ('created', 'last_modified', 'created_by', 'is_active')
    search_fields = ('title', 'text')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'last_modified', 'created_by')
