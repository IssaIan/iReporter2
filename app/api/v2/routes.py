from flask import Blueprint
from flask_restful import Api

from app.api.v2.views.incidentviews import (Admin, CommentUpdate, Incident,
                                            Incidents, LocationUpdate, Status,
                                            Type, MediaUpdate)
from app.api.v2.views.userviews import Login, Users

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two)
api.add_resource(Incidents, '/incidents')
api.add_resource(Incident, '/<incidenttype>/<int:incident_id>')
api.add_resource(Type, '/<incidenttype>')
api.add_resource(Status, '/incidents/<status>')
api.add_resource(Users, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(LocationUpdate, '/<incidenttype>/<int:incident_id>/location')
api.add_resource(CommentUpdate, '/<incidenttype>/<int:incident_id>/comment')
api.add_resource(Admin, '/admin/<incidenttype>/<int:incident_id>/statusupdate')
