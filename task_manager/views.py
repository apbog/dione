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


class RetrieveTask(generics.RetrieveAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class UpdateTask(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class EditTask(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
