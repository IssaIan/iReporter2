from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from app.api.v2.models.usermodels import UserModels


parser = reqparse.RequestParser()
parser.add_argument("first_name", type=str, required=True,
                    help="First name field is required")
parser.add_argument("last_name", type=str, required=True,
                    help="Last name field is required")
parser.add_argument("username", type=str, required=True,
                    help="Username field is required")
parser.add_argument("email", type=str, required=True,
                    help="Email field is required")
parser.add_argument("phonenumber", type=str, required=True,
                    help="Phone Number field is required")
parser.add_argument("password", type=str, required=True,
                    help="Password field is required")
parser.add_argument("confirm_password", type=str, required=True,
                    help="Confirm password field is required")


parser2 = reqparse.RequestParser()
parser2.add_argument('username', required=True,
                     help='This field cannot be blank')
parser2.add_argument('password', required=True,
                     help='This field cannot be blank')


class Users(Resource):
    """Handles user registration activity"""

    def __init__(self):
        self.db = UserModels()

    def post(self):
        data = parser.parse_args()
        first_name = data['first_name'].strip()
        last_name = data['last_name'].strip()
        username = data['username'].lower().strip()
        email = data['email'].strip()
        phonenumber = data['phonenumber'].strip()
        password = generate_password_hash(data['password'].strip())
        confirm_password = data['confirm_password'].strip()

        if self.db.validators(first_name) == False:
            return {'Error': 'Please enter a first name!'}, 422
        if self.db.validators(last_name) == False:
            return {'Error': 'Please enter a last name!'}, 422
        if self.db.validators(username) == False:
            return {'Error': 'Please enter a username!'}, 422
        if self.db.validators(email) == False or not self.db.validate_email(email):
            return {'Error': 'Please enter a valid email!'}, 422
        if self.db.validators(phonenumber) == False:
            return {'Error': 'Please enter a Phone Number!'}, 422
        if self.db.validators(password) == False:
            return {'Error': 'Please fill in a valid password!'}, 422
        if self.db.password_validation(confirm_password) == False:
            return {
                'Error': 'Please fill in a valid password! Password must be 8 characters long.'}, 422
        if self.db.get_user_name(username):
            return {'Error': 'Username already exists!'}, 401
        if self.db.get_email(email):
            return {'Error': 'Email already exists!'}, 401
        if self.db.checknumber(phonenumber):
            return {'Error': 'Phone Number already exists!'}, 401
        if not self.db.confirmpassword(password, confirm_password):
            return {'Error': 'Please ensure that both passwords match!'}, 401

        self.db.save_user(first_name, last_name, username,
                          email, phonenumber, password)
        return {'Message': 'User saved successfully'}, 201

    @jwt_required
    def get(self):
        result = self.db.get_all()
        if not self.db.isadmin(get_jwt_identity()):
            return{
                'Error': 'You are not an admin!'
            }, 403
        if result == []:
            return {
                'Error': 'No user found!'
            }, 404
        else:
            return jsonify(
                {
                    'Message': 'Records returned successfully!',
                    'Data': result
                }, 200)


class Login(Resource):
    """ Handles user login activity"""

    def __init__(self):
        self.db = UserModels()

    def post(self):
        data = parser2.parse_args()
        username = data['username'].lower()
        password = data['password']

        if self.db.validators(username):
            return {'Error': 'Please provide all credentials!'}, 422

        if self.db.validators(password):
            return {'Error': 'Please enter a valid password!'}, 422

        if not self.db.get_user_name(username):
            return {'Error': 'No user with that username found!'}, 404

        if not self.db.check_password(username, password):
            return {'Error': 'Wrong password!'}, 401

        login_token = self.db.user_login(username)
        if login_token:
            return jsonify({
                'Message': 'Welcome {}. You are now logged in!'.format(username),
                'Token': login_token,
                'User': self.db.get_user_name(username)
            }, 200)
