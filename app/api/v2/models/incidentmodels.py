import psycopg2
from flask import jsonify, json
from flask_restful import request
from psycopg2.extras import RealDictCursor
from db_config import Db


class IncidentModels(Db):

    def __init__(self):
        super().__init__()
        
    def save_incident(self, typee, description, status, location):
        self.cursor.execute(
            "INSERT INTO incidents(type, description, status, location)VALUES(%s, %s, %s, %s)",
            (typee, description, status, location))
        self.connect.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM incidents")
        incidentlist = self.cursor.fetchall()
        return incidentlist

    def find_by_id(self, id):
        self.cursor.execute(
            "SELECT * FROM incidents WHERE incident_id = {}".format(id))
        incident = self.cursor.fetchall()
        return incident

    def delete(self, id):
        self.find_by_id(id)
        self.cursor.execute("DELETE FROM incidents WHERE incident_id = {}".format(id))
        self.connect.commit()

    def updatelocation(self, location, id):
        self.cursor.execute(
            "UPDATE incidents SET location = '{}' WHERE incident_id = {}".format(location, id)
        )
        self.connect.commit()

    def updatecomment(self, comment, id):
        self.cursor.execute(
            "UPDATE incidents SET description = '{}' WHERE incident_id = {}".format(comment, id)
        )
        self.connect.commit()