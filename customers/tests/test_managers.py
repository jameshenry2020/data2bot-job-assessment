from rest_framework.test import APITestCase
from customers.models import User



class TestModelManagers(APITestCase):
    def test_email_validator_method_in_manager(self):
        self.assertRaises(ValueError, User.objects.create_user, email='dfdjhgfjhd', first_name='john', last_name='andrew', password='test4321')

    def test_email_not_provided_in_manager(self):
        self.assertRaises(ValueError, User.objects.create_user, email=' ', first_name='john', last_name='andrew', password='test4321')

    def test_create_user_return_instance(self):
        user=User.objects.create_user(email='johnp20@gmail.com', first_name='john', last_name='andrew', password='test4321')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'johnp20@gmail.com')

    def test_create_superuser_method(self):
        user=User.objects.create_superuser(email='johnp20@gmail.com', first_name='john', last_name='andrew', password='test4321')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_superuser_error_raise(self):
        self.assertRaises(ValueError, User.objects.create_superuser, email='', first_name='john', last_name='andrew', password='test4321')
    

    def test_superuser_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'is staff must be true for admin user'):
            User.objects.create_superuser(email='johnp21@gmail.com', first_name='john', last_name='andrew', password='test4321', is_staff=False)

    def test_superuser_is_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'is superuser must be true for admin user'):
            User.objects.create_superuser(email='johnp11@gmail.com', first_name='john', last_name='andrew', password='test4321', is_superuser=False)



