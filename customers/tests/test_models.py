from .test_setup import TestSetUp
from customers.models import User, Profile

# Create your tests here.


class TestUserModel(TestSetUp):

    def test_user_model_obj_str(self):
        user=User.objects.create_user(email='testuser3@gmail.com', first_name='emma',last_name='peter', password='test1234')
        self.assertEqual(user.__str__(), f"{user.first_name}")

    def test_user_get_full_name_method(self):
        user=User.objects.create_user(email='testuser1@gmail.com', first_name='emma',last_name='peter', password='test1234')
        full_name=f"{user.first_name} {user.last_name}"
        self.assertEqual(user.get_full_name, full_name)


    def test_profile_model_obj_str(self):
        user=User.objects.create_user(email='testuser12@gmail.com', first_name='emma',last_name='peter', password='test1234')
        profile=Profile.objects.get(user=user)
        self.assertEqual(profile.__str__(), f"{profile.user.first_name}-{profile.user.last_name}")

    
