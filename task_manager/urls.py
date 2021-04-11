from django.urls import path
from task_manager import views

urlpatterns = [
    path('create/', views.CreateTask.as_view()),
    path('list_create/', views.ListCreateTask.as_view()),
    path('list/', views.ListTask.as_view()),
    path('retrieve/<int:pk>/', views.RetrieveTask.as_view()),
    path('update/<int:pk>/', views.UpdateTask.as_view()),
    path('task/<int:pk>/', views.EditTask.as_view()),
]
