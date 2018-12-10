from flask_restful import Api, Resource
from flask import Blueprint
from app.api.v2.views.incidentviews import Incidents, Incident, LocationUpdate
from app.api.v2.views.userviews import Users, Login


version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two)
api.add_resource(Incidents, '/incidents')
api.add_resource(Incident, '/incidents/<int:incident_id>')
api.add_resource(Users, '/users')
api.add_resource(Login, '/login')
