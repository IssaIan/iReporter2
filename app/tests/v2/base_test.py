from unittest import TestCase
import json
from app import create_app
from flask import current_app
from db_config import Db

app = create_app("testing")


class BaseTest(TestCase):
    def setUp(self):

        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        Db().init_app(app)
        Db().create_tables()

        self.test_user = {
            "first_name": "Issa",
            "last_name": "Mwangi",
            "username": "issa",
            "password": "Maina9176",
            "confirm_password": "Maina9176",
            "phonenumber": "0722496986",
            "email": "issamwangi@gmail.com"
        }

        self.test_user2 = {
            "first_name": "Taby",
            "last_name": "Mwangi",
            "username": "njoki",
            "password": "Maina9176",
            "confirm_password": "Mwnjina9171",
            "phonenumber": "0722496986",
            "email": "njokimwangi@gmail.com"
        }

        self.test_user3 = {
            "first_name": "Gideon",
            "last_name": "Mwangi",
            "username": "kenn",
            "password": "Maina9176",
            "confirm_password": "Maina9176",
            "phonenumber": "0722496986",
            "email": "kennmwangi@gmail.com"
        }

        self.test_user4 = {
            "first_name": "Issa",
            "last_name": "Mwangi",
            "username": "issa",
            "password": "Maina9176",
            "confirm_password": "Maina9176",
            "phonenumber": "0722496986",
            "email": "issa2mwangi@gmail.com"
        }

        self.test_user5 = {
            "first_name": "Issa",
            "last_name": "Mwangi",
            "username": "issa2",
            "password": "Maina9176",
            "confirm_password": "Maina9176",
            "phonenumber": "0722496986",
            "email": "issamwangi@gmail.com"
        }
        
        self.test_incident = {
            "typee": "redflag",
            "description": "Corruption cases in Nairobi district",
            "status": "Draft",
            "location": "Nairobi"
        }
        self.update_incidentlocation = {
            "typee": "redflag",
            "description": "Corruption cases in Nairobi district",
            "status": "Draft",
            "location": "Nyeri"
        }
        self.update_incidentcomment = {
            "typee": "redflag",
            "description": "Police brutality at the CBD",
            "status": "Draft",
            "location": "Nairobi"
        }
        self.testlogin = {'username': self.test_user['username'],
                          'password': self.test_user['password']}

    def login(self):
        response = self.app.post('/api/v2/login',
                                 json=self.testlogin,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def registration(self):
        response = self.app.post('/api/v2/users',
                                 json=self.test_user,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def wrongpasswordregistration(self):
        response = self.app.post('/api/v2/users',
                                json = self.test_user2,
                                headers={'content-type': 'application/json'}
                                )
        return response

    def existingusernameregistration(self):
        response = self.app.post('/api/v2/users',
                                json = self.test_user4,
                                headers={'content-type': 'application/json'}
                                )
        return response
    
    def existingemailregistration(self):
        response = self.app.post('/api/v2/users',
                                json = self.test_user5,
                                headers={'content-type': 'application/json'}
                                )
        return response

    def user_token(self):
        self.registration()
        self.resp = self.login()
        self.tok = json.loads(self.resp.data)
        self.token = self.tok[0]['Token']
        print(self.token)
        return self.token

    def create_incident(self):
        token = self.user_token()
        response = self.app.post('/api/v2/incidents',
                                 json=self.test_incident,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content_type': 'application/json'}
                                 )
        return response

    def test_app_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def tearDown(self):
        Db().destroy_tables()
        self.app_context.pop()
