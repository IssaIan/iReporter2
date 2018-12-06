import psycopg2
from flask_restful import request
from db_config import *


class UserModels():
    def __init__(self):
        self.users = init_db()

    def save_user(self, user_id, first_name, last_name, username, email, date_created, password):
        curr = self.users.cursor()
        curr.execute(
            "INSERT INTO users(user_id, first_name, last_name, username, email, date_created, password)\
            VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (user_id, first_name, last_name, username, email, date_created, password))
            self.users.commit()

    def get_all(self):
        curr = self.users.cursor()
        curr.execute("SELECT * FROM users")
        rows = curr.fetchall()
        userlist = []

        for i, items in enumerate(rows):
            user_id, first_name, last_name, username, email, date_created, password = items
            data = dict(
                user_id = int(user_id),
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                date_created = date_created,
                password = password
            )
            userlist.append(data)
        return userlist

    