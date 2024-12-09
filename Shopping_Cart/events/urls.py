from django.urls import path
from .views import vendor_dashboard, add_product, user_dashboard

urlpatterns = [
    path('vendor/dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('vendor/add_product/', add_product, name='add_product'),
    path('user/dashboard/', user_dashboard, name='user_dashboard'),
]