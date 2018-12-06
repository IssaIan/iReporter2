import psycopg2
from flask_restful import request
from db_config import *


class IncidentModels():
    def __init__(self):
        self.incidents = init_db()

    def save_incident(self, incident_id, created_by, typee, description, status, location, created_on ):

        curr = self.incidents.cursor()
        curr.execute(
        "INSERT INTO incidents(incident_id, created_by, type, description, status, \
        location, created_on)VALUES(%s, %s, %s, %s, %s, %s, %s)", 
        (incident_id, created_by, typee, description, status, location, created_on))
        self.incidents.commit()

    def get_all(self):
        curr = self.incidents.cursor()
        curr.execute("SELECT * FROM incidents")
        rows = curr.fetchall()
        incidentlist = []
        
        for i, items in enumerate(rows):
            incident_id, created_by, typee, description, status, location, created_on = items
            data = dict(
                incident_id = int(incident_id),
                created_by = int(created_by),
                type = typee,
                description = description,
                status = status,
                location = location,
                created_on = created_on
            )
            incidentlist.append(data)
        return incidentlist

    def find_by_id(self, id):
        curr = self.incidents.cursor()
        curr.execute("SELECT * FROM incidents WHERE incident_id = (%s);", (id,))
        row = curr.fetchone()
        incident = []
        for items in enumerate(row):

            incident_id, created_by, typee, description, status, location, created_on = items
            data = dict(
               incident_id = int(incident_id),
               created_by = int(created_by),
               type = typee,
               description = description,
               status = status,
               location = location,
               created_on = created_on
            )
            incident.append(data)
        return incident


    def delete(self, id):
        curr = self.incidents.cursor()
        curr.execute("DELETE * FROM incidents WHERE incident_id = (%s);",(id,))
        self.incidents.commit()
        return True

    