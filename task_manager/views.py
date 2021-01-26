from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from task_manager.serializers import TaskSerializer
from rest_framework import generics
from task_manager.models import Task


# Create your views here.
@method_decorator(login_required, name='dispatch')
class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@method_decorator(login_required, name='dispatch')
class ListCreateTask(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@method_decorator(login_required, name='dispatch')
class ListTask(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
