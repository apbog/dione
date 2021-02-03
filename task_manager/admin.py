from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'created', 'created_by', 'is_active')
    list_display = ('title', 'text', 'created', 'created_by', 'is_active')
    list_filter = ('created', 'created_by', 'is_active')
    search_fields = ('title', 'text')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'created_by')
