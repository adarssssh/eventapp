from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import fetch_data, DecordetailView,CityDecorSearchView

urlpatterns = [
    path('fetch-data/', fetch_data, name='fetch_data'),
    path('decor/<str:vendor_id>/', DecordetailView.as_view(), name='vendor-detail'),
    path('decors/<str:city_name>/', CityDecorSearchView.as_view(), name='city_vendor_search'),
]