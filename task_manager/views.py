from django.shortcuts import render
from task_manager.serializers import TaskSerializer
from rest_framework import generics
from task_manager.models import Task


# Create your views here.
class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer


class ListTask(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
