from django.urls import path
from task_manager import views

urlpatterns = [
    path('task/create/', views.CreateTask.as_view()),
]