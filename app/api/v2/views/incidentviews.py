import psycopg2
from flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.v2.models.incidentmodels import IncidentModels

class GetError():
    def notFound(self):
        return {
            'Message':'Resource not found' 
        }, 404

class Incidents(Resource, GetError):
    def __init__(self):
        self.db = IncidentModels()

    def post(self):

        data = request.get_json()
        incident_id = data['incident_id']
        created_by = data['created_by']
        typee = data['typee']
        description = data['description']
        status = data['status']
        location = data['location']
        created_on = data['created_on']
        self.db.save_incident(incident_id,created_by, typee,description, status, location, created_on)           
        return make_response(jsonify({
            'Message' : 'Success'
        }), 201)

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

class Incident(Resource, GetError):
    def __init__(self):
        self.db = IncidentModels()
        
    def delete(self, incident_id):
        self.db.delete(incident_id)
        if True:
            return {
                'Message':'Successfully deleted'
            }, 200
        else:
            return self.notFound()
    def get(self, incident_id):
        inci = self.db.find_by_id(incident_id)

        return make_response(jsonify({
            'Message':'Incident returned successfully',
            'Data':inci
        }), 200)
    

    
    def update(self):
        pass
