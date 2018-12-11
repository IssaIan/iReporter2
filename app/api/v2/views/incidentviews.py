import psycopg2
from flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.v2.models.incidentmodels import IncidentModels
import datetime


class Incidents(Resource):
    def __init__(self):
        self.db = IncidentModels()

    def post(self):

        data = request.get_json()
        typee = data['typee']
        description = data['description']
        status = data['status']
        location = data['location']
        created_on = datetime.datetime.now()

        resp =None
        if typee.isspace() or typee == "":
            resp = {'Message' : 'Type cannot be empty!'}
        if description.isspace() or description == "":
            resp = {'Message' : 'Description cannot be empty!'}
        if location.isspace() or description == "":
            resp = {'Message' : 'Location cannot be empty!'}
        if resp is not None:
            return jsonify(resp)

        self.db.save_incident(typee, description, status, location)
        return make_response(jsonify({
            'Message': 'Record successfully saved!'
        }), 201)

    def get(self):
        result = self.db.get_all()
        if result == []:
            return jsonify({
                'Message' : 'Record not found!'
            }, 404)
        else:
            return make_response(jsonify(
                {
                    'Message': 'Records returned successfully',
                    'Data': result
                }
            ), 200)


class Incident(Resource):
    def __init__(self):
        self.db = IncidentModels()

    def delete(self, incident_id):
        if not self.db.find_by_id(incident_id):
            return jsonify({
                'Message' : 'The record you are trying to delete has not been found!'
            })
        self.db.delete(incident_id)
        return {
            'Message': 'Record successfully deleted from the database!'
        }, 200

    def get(self, incident_id):
        incident = self.db.find_by_id(incident_id)
        if incident == []:
            return jsonify({
                'Message' : 'Record not found!'
            }, 404)
        return make_response(jsonify({
            'Message': 'Incident returned successfully',
            'Data': incident
        }), 200)


class LocationUpdate(Resource):
    def __init__(self):
        self.db = IncidentModels()

    def patch(self, incident_id):
        data = request.get_json()
        location = data['location']
        incident = self.db.find_by_id(incident_id)
        if incident:
            self.db.updatelocation(location, incident_id)
            return make_response(jsonify({
                'Message': 'Updated incident location',
                'data' : incident 
            }), 200)
        return jsonify({
                'Message' : 'Record not found!'
            }, 404)


class CommentUpdate(Resource):
    def __init__(self):
        self.db = IncidentModels()

    def patch(self, incident_id):
        data = request.get_json()
        comment = data['description']
        incident = self.db.find_by_id(incident_id)
        if incident:
            self.db.updatecomment(comment, incident_id)
            return make_response(jsonify({
                'Message' : 'Updated incident comment',
                'data' : incident 
            }), 200)
        return jsonify({
            'Message' : 'Record not found!'
        }, 404)