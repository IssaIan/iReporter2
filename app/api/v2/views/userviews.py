import psycopg2
from flask_restful import Resource
from flask import request, jsonify, make_response
from app.api.v2.models.usermodels import UserModels

class GetError():
    def notFound(self):
        return{
            'Message':'Resource not found'
        }, 404
    

class Users(Resource, GetError):
    def __init__(self):
        self.db = UserModels()

    def post(self):
        data = request.get_json()
        user_id = data['user_id']
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        date_created = data['date_created']
        password = data['password']
        
        self.db.save_user(user_id, first_name, last_name, username, email, date_created, password)
        return make_response(jsonify(
            {
                'Message':'User saved successfully'
            }
        ), 201)

    def get(self):
        result = self.db.get_all()
        if result == []:
            return self.notFound()
        else:
            return make_response(jsonify(
                {
                    'Message':'Records returned successfully',
                    'Data':result
                }
            ), 200)


            