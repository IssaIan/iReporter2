from flask_restful import Api
from flask import Blueprint
from app.api.v2.views.incidentviews import Admin, Incidents, Incident, LocationUpdate, CommentUpdate, Type, Status
from app.api.v2.views.userviews import Users, Login
version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two)
api.add_resource(Incidents, '/incidents')
api.add_resource(Incident, '/<incidenttype>/<int:incident_id>')
api.add_resource(Type, '/<incidenttype>')
api.add_resource(Status, '/<status>')
api.add_resource(Users, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(LocationUpdate, '/<incidenttype>/<int:incident_id>/location')
api.add_resource(CommentUpdate, '/<incidenttype>/<int:incident_id>/comment')
api.add_resource(Admin, '/admin/<incidenttype>/<int:incident_id>/statusupdate')

