from task_manager.serializers import TaskSerializer
from rest_framework import generics
from task_manager.models import Task


class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ListCreateTask(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ListTask(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
