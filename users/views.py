from django.http import Http404
from django.shortcuts import render, redirect, reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import login, logout


class RegisterAPI(APIView):
    def post(self, request):
        register_serializer = RegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            user = register_serializer.save()
            return Response(data={'username': user.username, 'email': user.email}, status=200)
        else:
            return Response(data={'username': register_serializer.errors.get('username', None),
                                  'email': register_serializer.errors.get('email', None),
                                  'password': register_serializer.errors.get('password', None)}, status=201)


class LoginAPI(APIView):
    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            login(request, user)
            token = Token.objects.create(user=user)
            return Response(data={
                'token': token.key,
                'login': True
            }, status=200)
        else:
            return Response(status=201)


class LogoutAPI(APIView):
    def post(self, request):
        key = request.COOKIES['TokenAuthentication']
        logout(request)
        Token.objects.get(key=key).delete()
        return Response(data={
            'detail': 'you are logged out now',
            'logout': True
        })


def login_form(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        raise Http404('you are now logged in')
    return render(request, 'users/login.html')


def register_form(request):
    if request.user.is_authenticated:
        raise Http404('you are now logged in')
    return render(request, 'users/register.html')


def logout_form(request):
    if request.user.is_authenticated:
        return render(request, 'users/logout.html')
    else:
        return redirect(reverse('login'))
