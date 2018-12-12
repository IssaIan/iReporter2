import psycopg2
from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
import datetime
from app.api.v2.models.usermodels import UserModels


class Users(Resource):
    def __init__(self):
        self.db = UserModels()

    def post(self):
        data = request.get_json()
        first_name = data['first_name'].strip()
        last_name = data['last_name'].strip()
        username = data['username'].lower().strip()
        email = data['email'].strip()
        phonenumber = data['phonenumber'].strip()
        date_created = datetime.datetime.now()
        password = generate_password_hash(data['password'].strip())
        is_admin = data['is_admin']
        confirm_password = data['confirm_password'].strip()

        resp = None
        if password.isspace() or len(password.strip()) < 8:
            resp = {
                'Message': 'Please fill in a valid password! Password must be 8 characters long!'}
        if email.isspace() or not self.db.validate_email(email):
            resp = {'Message': 'Please enter a valid email!'}
        if first_name.isspace() or first_name == "":
            resp = {'Message': 'Please enter a first name!'}
        if last_name.isspace() or last_name == "":
            resp = {'Message': 'Please enter a last name!'}
        if username.isspace() or username == "":
            resp = {'Message': 'Please enter a username!'}
        if is_admin != 'true' and is_admin != 'false': 
            resp = {'Message' : 'Please enter true or false'}

        if resp is not None:
            return resp, 422

        user = self.db.get_user_name(username)
        emailconfirm = self.db.get_email(email)

        if user:
            return {'Message': 'Username already exists!'}, 401
        if emailconfirm:
            return {'Message': 'Email already exists!'}, 401
        if not self.db.confirmpassword(password, confirm_password):
            return {'Message': 'Please ensure that both passwords match!'}, 401

        self.db.save_user(first_name, last_name, username,
                          email, phonenumber, password, is_admin)
        return {'Message': 'User saved successfully'}, 201

    def get(self):
        result = self.db.get_all()
        if result == []:
            return {
                'Message': 'No user found!'
            }, 404
        else:
            return make_response(jsonify(
                {
                    'Message': 'Records returned successfully!',
                    'Data': result
                }
            ), 200)


class Login(Resource):
    def __init__(self):
        self.db = UserModels()

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        user = self.db.get_user_name(username)

        if username.isspace() or username == "":
            return {'Message': 'Please provide all credentials!'}, 422

        if password.isspace() or password is None:
            return {'Message': 'Please enter a valid password!'}, 422

        if not user:
            return {'Message': 'No user with that username found!'}, 404

        if not self.db.check_password(username, password):
            return {'Message': 'Wrong password!'}, 401

        login_token = self.db.user_login(username)
        if login_token:
            return jsonify({
                'Message': 'You are now logged in!',
                'Token': login_token,
                'User': user
            }, 200)
