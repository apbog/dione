from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    # path('landing/', views.landing_page, name='landing_page'),
    # path('product/', views.product_page, name='product_page'),
]
