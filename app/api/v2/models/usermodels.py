import re
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from db_config import Db


class UserModels(Db):
    """ Handles interaction with the users table in the database.
    Contains queries to interact with the users table in the database"""

    def __init__(self):
        super().__init__()

    def save_user(self, first_name, last_name, username, email, phonenumber, password):
        self.cursor.execute(
            "INSERT INTO users(first_name, last_name, username, email, phonenumber, password)VALUES(%s, %s, %s, %s, %s, %s)",
            (first_name, last_name, username, email, phonenumber, password))
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
            incident_id = user_id.get('user_id')
            return incident_id
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
            "SELECT * FROM users WHERE user_id = {} and is_admin = 'true'".format(
                userid)
        )
        user = self.cursor.fetchall()
        return user

    def promoteuser(self):
        self.cursor.execute(
            "UPDATE users SET is_admin='true' where username = 'admin'"
        )
        self.connect.commit()

    def create_admin(self):
        pas = generate_password_hash('adminuser')

        if self.get_user_name('admin'):
            return 'Admin already exists!'
        self.save_user('issa', 'mwangi', 'admin',
                       'issaadmin@gmail.com', '0799123456', pas)
        self.promoteuser()

    def password_validation(self, password):
        if len(password) >= 8 and password.isalnum():
            return True
        return False

    def checknumber(self, phonenumber):
        self.cursor.execute(
            "SELECT * FROM users where phonenumber = {}".format(phonenumber)
        )
        user = self.cursor.fetchall()
        return user
