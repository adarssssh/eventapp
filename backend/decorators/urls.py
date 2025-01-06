from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import fetch_data

urlpatterns = [
    path('fetch-data/', fetch_data, name='fetch_data'),
]