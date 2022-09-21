import ast
from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from customers.models import User

class TestSetUp(APITestCase):
 
    def setUp(self):
        self.fake = Faker()
        self.register_url=reverse('register')
        self.login_url=reverse('customer-login')
        self.profile_url=reverse('profile-update')
        self.orders_url=reverse("orders")

        self.user_data={
            'email':self.fake.email(),
            'first_name':'john',
            'last_name':'doe',
            'password':'testpwd123',
            'retype_password':'testpwd123'
        }
        self.user_error={
            'email':'',
            'first_name':'john',
            'last_name':'doe',
            'password':'testpwd123',
            'retype_password':'testpwd123'
        }

        User.objects.create_user(email='anotheruser@gmail.com',first_name='sammy', last_name='rita',password=self.user_data['password'])
        self.user=self.client.post(self.login_url, {'email':'anotheruser@gmail.com','password':self.user_data['password']})
        self.auth_tokens=ast.literal_eval(self.user.data['tokens'])
        self.token=self.auth_tokens['access']
        self.api_authorization()
        

    def api_authorization(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        return super().setUp()

    def tearDown(self):

        return super().tearDown()