import re

from rest_framework import serializers

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
