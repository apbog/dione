from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='landing_page'),
    path('landing/', views.landing_page, name='landing_page'),
]
