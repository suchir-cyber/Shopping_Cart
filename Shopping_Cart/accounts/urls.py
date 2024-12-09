from django.urls import path
from .views import home, register_user, register_vendor

urlpatterns = [
    path('', home, name='home'),
    path('register/user/', register_user, name='register_user'),
    path('register/vendor/', register_vendor, name='register_vendor'),
]