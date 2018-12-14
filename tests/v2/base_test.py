from unittest import TestCase
import json
from flask import current_app
from app import create_app
from db_config import Db
from app.api.v2.models.usermodels import UserModels


class BaseTest(TestCase):
    def setUp(self):

        app = create_app(config_name="testing")
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        Db().init_app(app)
        Db().create_tables()
        UserModels().create_admin()

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
        self.test_user6 = {
            "first_name": "",
            "last_name": "Mwangi",
            "username": "issa22",
            "password": "Maina9176",
            "confirm_password": "Maina9176",
            "phonenumber": "0722496986",
            "email": "issamwangi22@gmail.com"
        }
        self.test_user7 = {
            "first_name": "taby",
            "last_name": "Mwangi",
            "username": "issa22",
            "password": "Mai",
            "confirm_password": "Mai",
            "phonenumber": "0722496986",
            "email": "issamwangi22@gmail.com"
        }


        self.test_incident = {
            "typeofincident": "redflag",
            "description": "Corruption cases in Nairobi district",
            "location": "Nairobi"
        }
        self.update_incidentlocation = {
            "typeofincident": "redflag",
            "description": "Corruption cases in Nairobi district",
            "location": "Nyeri"
        }
        self.update_incidentcomment = {
            "typeofincident": "redflag",
            "description": "Police brutality at the CBD",
            "location": "Nairobi"
        }
        self.update_incidentstatus = {
            "typeofincident": "redflag",
            "description": "Police brutality at the CBD",
            "status": "Under-investigation",
            "location": "Nairobi"
        }

        self.userlogin = {'username': self.test_user['username'],
                          'password': self.test_user['password']}

        self.superadmin = {'username': 'admin',
                           'password': 'adminuser'}

        self.loginnormaluser = {'username': self.test_user5['username'],
                                'password': self.test_user5['password']}

    
    def loginsuperadmin(self):
        response = self.app.post('/api/v2/login',
                                 json=self.superadmin,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def login(self):
        response = self.app.post('/api/v2/login',
                                 json=self.userlogin,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def registration(self):
        response = self.app.post('/api/v2/users',
                                 json=self.test_user,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def registerwithoutfirstname(self):
        response = self.app.post('/api/v2/users',
                                 json=self.test_user6,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def userregistration(self):
        response = self.app.post('/api/v2/users',
                                 json=self.test_user5,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def loginuser(self):
        response = self.app.post('/api/v2/login',
                                 json=self.loginnormaluser,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def wrongpasswordregistration(self):
        response = self.app.post('/api/v2/users',
                                 json=self.test_user2,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def existingusernameregistration(self):
        response = self.app.post('/api/v2/users',
                                 json=self.test_user4,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def existingemailregistration(self):
        response = self.app.post('/api/v2/users',
                                 json=self.test_user5,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def invalidpasswordregistration(self):
        response = self.app.post('/api/v2/users',
                                json=self.test_user7,
                                headers={'content-type': 'application/json'}
                                )
        return response

    def superadmintoken(self):
        self.resp = self.loginsuperadmin()
        self.tok = json.loads(self.resp.data)
        self.token = self.tok[0]['Token']
        return self.token

    def user1_token(self):
        self.registration()
        self.resp = self.login()
        self.tok = json.loads(self.resp.data)
        print(self.tok)
        self.token = self.tok[0]['Token']
        print(self.token)
        return self.token

    def user_token(self):
        self.userregistration()
        self.resp = self.loginuser()
        self.tok = json.loads(self.resp.data)
        self.token = self.tok[0]['Token']
        return self.token

    def create_incident(self):
        token = self.user1_token()
        response = self.app.post('/api/v2/incidents',
                                 json=self.test_incident,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def normal_user_create_incident(self):
        token = self.user_token()
        response = self.app.post('/api/v2/incidents',
                                 json=self.test_incident,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def test_app_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def tearDown(self):
        Db().destroy_tables()
        self.app_context.pop()
