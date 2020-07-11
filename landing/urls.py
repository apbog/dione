from django.urls import path
from landing.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page')
]
