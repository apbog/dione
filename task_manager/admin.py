from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'text')
    list_display = ['title', 'text', 'created']
    list_filter = ('created',)
    search_fields = ['title', 'text']
    date_hierarchy = 'created'
    readonly_fields = ['title']
