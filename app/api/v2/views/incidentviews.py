import psycopg2
from flask_restful import Resource
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v2.models.incidentmodels import IncidentModels
from app.api.v2.models.usermodels import UserModels
import datetime


class Incidents(Resource):
    def __init__(self):
        self.db = IncidentModels()

    @jwt_required
    def post(self):

        data = request.get_json()
        created_by = get_jwt_identity()
        typee = data['typee']
        description = data['description']
        location = data['location']

        resp = None
        if typee.isspace() or typee == "":
            resp = {'Message': 'Type cannot be empty!'}
        if description.isspace() or description == "":
            resp = {'Message': 'Description cannot be empty!'}
        if location.isspace() or description == "":
            resp = {'Message': 'Location cannot be empty!'}
        if resp is not None:
            return jsonify(resp)

        self.db.save_incident(created_by, typee, description, location)
        return {
            'Message': 'Record successfully saved!'
        }, 201

    def get(self):
        result = self.db.get_all()
        if result == []:
            return {
                'Message': 'Record not found!'
            }, 404
        else:
            return jsonify(
                {
                    'Message': 'Records returned successfully',
                    'Data': result
                }, 200)


class Incident(Resource):
    def __init__(self):
        self.db = IncidentModels()

    @jwt_required
    def delete(self, incident_id):
        userincidents = self.db.get_by_user_id(get_jwt_identity())
        if not self.db.find_by_id(incident_id):
            return {
                'Message': 'The record you are trying to delete has not been found!'
            }, 404
        if not userincidents:
            return jsonify(
                {
                    'Message': 'You cannot delete an incident that does not belong to you!'
                }, 401
            )
        self.db.delete(incident_id, get_jwt_identity())
        return {
            'Message': 'Record successfully deleted from the database!'
        }, 200

    def get(self, incident_id):
        incident = self.db.find_by_id(incident_id)
        if incident == []:
            return {
                'Message': 'Record not found!'
            }, 404
        return jsonify({
            'Message': 'Record returned successfully',
            'Data': incident
        }, 200)


class LocationUpdate(Resource):
    def __init__(self):
        self.db = IncidentModels()

    @jwt_required
    def patch(self, incident_id):
        data = request.get_json()
        location = data['location']
        incident = self.db.find_by_id(incident_id)
        userincidents = self.db.get_by_user_id(get_jwt_identity())
        if not incident:
            return {
                'Message': 'Record not found!'
            }, 404
        if not userincidents:
            return {
                'Message': 'You cannot update an incident that does not belong to you!'
            }, 401
        self.db.updatelocation(location, incident_id, get_jwt_identity())
        return jsonify({
            'Message': 'Updated incident location successfully!',
            'data': incident
        }, 200)


class CommentUpdate(Resource):
    def __init__(self):
        self.db = IncidentModels()

    @jwt_required
    def patch(self, incident_id):
        data = request.get_json()
        comment = data['description']
        incident = self.db.find_by_id(incident_id)
        userincidents = self.db.get_by_user_id(get_jwt_identity())
        if not incident:
            return {
                'Message': 'Record not found!'
            }, 404
        if not userincidents:
            return {
                'Message': 'You cannot update an incident that does not belong to you!'
            }, 401
        self.db.updatecomment(comment, incident_id, get_jwt_identity())
        return jsonify({
            'Message': 'Updated incident comment successfully!',
            'data': incident
        }, 200)


class Admin(Resource):
    def __init__(self):
        self.db = IncidentModels()
        self.admin = UserModels()

    @jwt_required
    def patch(self, incident_id):
        data = request.get_json()
        status = data['status']
        incident = self.db.find_by_id(incident_id)
        
        if not self.admin.isadmin(get_jwt_identity()):
            return{
                'Message' : 'You are not an admin!'
            }, 403
        if not incident:
            return {
                'Message': 'Record not found!'
            }, 404
        self.db.updatestatus(status, incident_id)
        return jsonify({
            'Message': 'Updated incident status successfully!',
            'data': incident
        }, 200)
