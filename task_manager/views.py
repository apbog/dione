from django.shortcuts import render
from task_manager.serializers import TaskSerializer
from rest_framework import generics


# Create your views here.
class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer
