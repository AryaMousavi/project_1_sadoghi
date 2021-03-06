import re

from rest_framework import serializers
from django.contrib.auth import authenticate, login
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'avatar')

    def validate_username(self, username):
        if re.match(r'^[\w.]{1,25}$', username):
            return username
        raise serializers.ValidationError(['username is incorrect'])

    def validate_email(self, email):
        if re.match(r'^[\w.]+@gmail.com$', email):
            return email
        raise serializers.ValidationError('email is incorrect')

    def validate_password(self, password):
        if re.match(r'^[\w\W.]{8,}$', password):
            return password
        raise serializers.ValidationError('password is incorrect')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        print(validated_data.get('owner'))
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            if User.objects.filter(email=email).exists():
                user = authenticate(self.context.get('request'), email=email, password=password)
            else:
                msg = {
                    'detail': 'email is not registered',
                    'register': False
                }
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'must fill out "email" and "password"'
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data






