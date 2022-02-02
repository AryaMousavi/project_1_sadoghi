from django.test import TestCase
from ..models import User
from django.shortcuts import reverse


class LoginTests(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(
            username='arya266',
            email='arya2661384@gmail.com',
            password='123456789'
        )

    def test_login(self):
        response = self.client.post(reverse('login'), data={
            'email': 'arya2661384@gmail.com',
            'password': '123456789',
        })
        print(response.content.decode())
