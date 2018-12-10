import psycopg2
from flask import jsonify, json
from flask_restful import request
from psycopg2.extras import RealDictCursor
from db_config import *


class IncidentModels():
    def __init__(self):
        self.incidents = init_db()

    def save_incident(self, typee, description, status, location):

        curr = self.incidents.cursor(cursor_factory=RealDictCursor)
        curr.execute(
            "INSERT INTO incidents(type, description, status, location)VALUES(%s, %s, %s, %s)",
            (typee, description, status, location))
        self.incidents.commit()

    def get_all(self):
        curr = self.incidents.cursor(cursor_factory=RealDictCursor)
        curr.execute("SELECT * FROM incidents")
        incidentlist = curr.fetchall()
        return incidentlist

    def find_by_id(self, id):
        curr = self.incidents.cursor(cursor_factory=RealDictCursor)
        curr.execute(
            "SELECT * FROM incidents WHERE incident_id = {}".format(id))
        incident = curr.fetchall()
        return incident

    def delete(self, id):
        self.find_by_id(id)
        curr = self.incidents.cursor(cursor_factory=RealDictCursor)
        curr.execute("DELETE FROM incidents WHERE incident_id = {}".format(id))
        self.incidents.commit()

    