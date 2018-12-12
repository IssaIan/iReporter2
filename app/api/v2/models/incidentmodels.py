import psycopg2
from flask import jsonify, json
from flask_restful import request
from psycopg2.extras import RealDictCursor
from db_config import Db


class IncidentModels(Db):

    def __init__(self):
        super().__init__()
        
    def save_incident(self, created_by, typee, description, location):
        self.cursor.execute(
            "INSERT INTO incidents(created_by, type, description, location)VALUES(%s, %s, %s, %s)",
            (created_by, typee, description, location))
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

    def delete(self, id, user_id):
        self.find_by_id(id)
        self.cursor.execute("DELETE FROM incidents WHERE incident_id = {} and created_by = {}".format(id, user_id))
        self.connect.commit()

    def updatelocation(self, location, id, user_id):
        self.cursor.execute(
            "UPDATE incidents SET location = '{}' WHERE incident_id = {} and created_by = {}".format(location, id, user_id)
        )
        self.connect.commit()

    def updatecomment(self, comment, id, user_id):
        self.cursor.execute(
            "UPDATE incidents SET description = '{}' WHERE incident_id = {} and created_by = {}".format(comment, id, user_id)
        )
        self.connect.commit()

    def get_by_user_id(self, id):
        self.cursor.execute(
            "SELECT * FROM incidents WHERE created_by = {}".format(id)
        )
        incident = self.cursor.fetchall()
        return incident

    def updatestatus(self, status, id):
        self.cursor.execute(
            "UPDATE incidents SET status = '{}' WHERE incident_id = {}".format(status, id)
        )
        self.connect.commit()