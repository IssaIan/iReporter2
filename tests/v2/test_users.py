import json
from tests.v2.base_test import BaseTest

class UsersTest(BaseTest):

    def test_create_user(self):
        response = self.registration()
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'User saved successfully')
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        self.registration()
        response = self.login()
        result = json.loads(response.data)
        self.assertEqual(result[0]['Message'], 'You are now logged in!')
        self.assertEqual(response.status_code, 200)

    def test_login_unregistered_user(self):
        response = self.login()
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'No user with that username found!')
        self.assertEqual(response.status_code, 404)

    def test_unmatching_password_during_registration(self):
        response = self.wrongpasswordregistration()
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Please ensure that both passwords match!')
        self.assertEqual(response.status_code, 401)
    
    def test_existingusername(self):
        self.registration()
        response = self.existingusernameregistration()
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Username already exists!')
        self.assertEqual(response.status_code, 401)

    def test_existingemail(self):
        self.registration()
        response = self.existingemailregistration()
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Email already exists!')
        self.assertEqual(response.status_code, 401)

    def test_getallusers(self):
        self.registration()
        response = self.app.get('/api/v2/users')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Records returned successfully!')
        self.assertEqual(response.status_code, 200)
        
    def test_firstnamemissing(self):
        response = self.registerwithoutfirstname()
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Please enter a first name!')
        
    
    
