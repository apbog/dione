from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE)
    # TODO: Add is_active field

    def __str__(self):
        return self.title
