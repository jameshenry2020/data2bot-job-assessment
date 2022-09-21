from xml.dom import ValidationErr
from .test_setup import TestSetUp
from customers.models import Profile, User 


class TestUserViews(TestSetUp):
    def test_user_cannot_be_register_without_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_enter_wrong_data_to_register(self):
        res = self.client.post(self.register_url, self.user_error, format='json')
        self.assertEqual(res.status_code, 400)
        
    
    def test_user_can_register(self):
        res = self.client.post(self.register_url, self.user_data, format='json')  
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['email'], self.user_data['email'])

    def test_user_can_login(self):
        self.client.post(self.register_url, self.user_data, format='json')
        data={
            'email':self.user_data['email'],
            'password':self.user_data['password']
        }
        response =self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, 200)


    def test_user_can_update_profile(self):
         response=self.client.patch(self.profile_url,  {"first_name":"peter", "last_name":"shedrack", "phone_number":"+2349080886406", "country":"USA", "city":"Newyork"})
         self.assertEqual(response.status_code, 200)
            


        

