from django.shortcuts import reverse
from django.test import TestCase


class RegisterTests(TestCase):

    def test_right_register(self):
        data = {
            'username': 'arya266',
            'email': 'arya2661384@gmail.com',
            'password': '1234'
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['username'], data['username'])
        self.assertEqual(response.json()['email'], data['email'])

    def test_wrong_register(self):
        data = {
            'username': '#arya+salam',
            'email': '@gmail.com',
            'password': '1234'
        }
        response = self.client.post(reverse('register'), data=data)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['username'], data['username'])
        self.assertEqual(response.json()['email'], data['email'])
