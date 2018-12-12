import psycopg2
import re
from flask_restful import request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import get_jwt_identity, create_access_token
from db_config import Db


class UserModels(Db):
    def __init__(self):
        super().__init__()

    def save_user(self, first_name, last_name, username, email, phonenumber, password, is_admin):
        self.cursor.execute(
            "INSERT INTO users(first_name, last_name, username, email, phonenumber, password, is_admin)VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, username, email, phonenumber, password, is_admin))
        self.connect.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM users")
        userlist = self.cursor.fetchall()
        return userlist

    def get_user_name(self, username):
        self.cursor.execute(
            "SELECT * FROM users WHERE username='{}'".format(username))
        user = self.cursor.fetchall()
        return user

    def get_email(self, email):
        self.cursor.execute(
            "SELECT * FROM users WHERE email='{}'".format(email))
        row = self.cursor.fetchone()
        if row:
            email = row.get('email')
            return email
        else:
            return None

    def validate_email(self, email):
        valid = re.match(
            "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip())
        if valid is None:
            return False

        return True

    def get_id(self, username):
        self.cursor.execute(
            "SELECT user_id FROM users WHERE username='{}'".format(username))
        user_id = self.cursor.fetchone()
        if user_id:
            id = user_id.get('user_id')
            return id
        else:
            return None

    def check_password(self, username, password):
        dbpassword = self.get_password(username)
        return check_password_hash(dbpassword, password)

    def get_password(self, username):
        self.cursor.execute(
            "SELECT password FROM users WHERE username='{}'".format(username))
        pas = self.cursor.fetchone()
        if pas:
            password = pas.get('password')
            return password
        else:
            return None

    def generate_jwt_token(self, username):
        self.user_id = self.get_id(username)
        token = create_access_token(identity=self.user_id)
        return token

    def user_login(self, username):
        token = self.generate_jwt_token(username)
        return token

    def confirmpassword(self, password, confirm_password):
        return check_password_hash(password, confirm_password)

    def isadmin(self, userid):
        self.cursor.execute(
            "SELECT * FROM users WHERE user_id = {} and is_admin = 'true'".format(userid)
        )
        user = self.cursor.fetchall()
        return user