from django.urls import path
from .views import fetch_data, VendorDetailView, CityVendorSearchView


urlpatterns = [
    # path('fetch-data/', fetch_data, name='fetch_data_venue'),
    path('vendor/<str:vendor_id>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/<str:city_name>/', CityVendorSearchView.as_view(), name='city_vendor_search'),
]


