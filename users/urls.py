from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterAPI, register_form, login_form, LoginAPI, LogoutAPI, logout_form

urlpatterns = [
    path('login-api/', LoginAPI.as_view(), name='login_api'),
    path('register-api/', RegisterAPI.as_view(), name='register_api'),
    path('logout-api/', LogoutAPI.as_view(), name='logout_api'),
    path('logout/', logout_form, name='logout'),
    path('login/', login_form, name='login'),
    path('register/', register_form, name='register'),
]
