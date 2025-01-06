from django.urls import path
from .views import fetch_data


urlpatterns = [
    path('fetch-data/', fetch_data, name='fetch_data_venue')
]


