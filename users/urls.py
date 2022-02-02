from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterAPI, register_form, login_form

urlpatterns = [
    path('login-api/', obtain_auth_token, name='login_api'),
    path('register-api/', RegisterAPI.as_view(), name='register_api'),
    path('login/', login_form, name='login'),
    path('register/', register_form, name='register'),
]
