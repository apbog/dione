from django.urls import path
from task_manager import views

urlpatterns = [
    path('create/', views.CreateTask.as_view()),
    path('list_create/', views.ListCreateTask.as_view()),
    path('list/', views.ListTask.as_view()),
]
