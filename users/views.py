from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import RegisterSerializer


class RegisterAPI(APIView):
    def post(self, request):
        register_serializer = RegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            user = register_serializer.save()
            return Response(data={'username': user.username, 'email': user.email}, status=200)
        else:
            return Response(data={'username': register_serializer.errors.get('username', None),
                                  'email': register_serializer.errors.get('email', None),
                                  'password': register_serializer.errors.get('password', None)}, status=200)


def login_form(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return Http404('Ok')
    return render(request, 'users/login.html')


def register_form(request):
    if request.user.is_authenticated:
        return Http404('Ok')
    return render(request, 'users/register.html')
