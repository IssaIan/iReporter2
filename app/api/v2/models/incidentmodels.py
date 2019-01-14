import re

from db_config import Db


class IncidentModels(Db):
    """Handles interaction with the incidents tables in the database
    Queries that interact with the incident table in the database are contained here"""

    def __init__(self):
        super().__init__()

    def save_incident(self, created_by, typeofincident, description, location, media_path):
        self.cursor.execute(
            "INSERT INTO incidents(created_by, type, description, location media_path)VALUES(%s, %s, %s, %s, %s)",
            (created_by, typeofincident, description, location, media_path))
        self.connect.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM incidents")
        incidentlist = self.cursor.fetchall()
        return incidentlist

    def find_by_id(self, incident_id):
        self.cursor.execute(
            "SELECT * FROM incidents WHERE incident_id = {}".format(incident_id))
        incident = self.cursor.fetchall()
        return incident

    def delete(self, incident_id, user_id):
        self.find_by_id(incident_id)
        self.cursor.execute(
            "DELETE FROM incidents WHERE incident_id = {} and created_by = {}".format(incident_id, user_id))
        self.connect.commit()

    def updatelocation(self, location, incident_id, user_id):
        self.cursor.execute(
            "UPDATE incidents SET location = '{}' WHERE incident_id = {} and created_by = {}".format(
                location, incident_id, user_id)
        )
        self.connect.commit()

    def updatecomment(self, comment, incident_id, user_id):
        self.cursor.execute(
            "UPDATE incidents SET description = '{}' WHERE incident_id = {} and created_by = {}".format(
                comment, incident_id, user_id)
        )
        self.connect.commit()

    def updatemedia(self, media_path, incident_id, user_id):
        self.cursor.execute(
            "UPDATE incidents SER media_path = '{}' WHERE incident_id = {} and created_by ={}".format(
                media_path, incident_id, user_id)
        )
        self.connect.commit()

    def get_by_user_id(self, user_id, incident_id):
        self.cursor.execute(
            "SELECT * FROM incidents WHERE created_by = {} and incident_id = {}".format(user_id, incident_id)
        )
        incident = self.cursor.fetchone()
        return incident

    def updatestatus(self, status, incident_id):
        self.cursor.execute(
            "UPDATE incidents SET status = '{}' WHERE incident_id = {}".format(
                status, incident_id)
        )
        self.connect.commit()

    def get_user_from_incident(self, incident_id):
        incident = self.find_by_id(incident_id)
        user = incident[0]['created_by']
        return user

    def get_user_email(self, incident_id):
        user = self.get_user_from_incident(incident_id)

        self.cursor.execute(
            "SELECT * FROM users WHERE user_id = {}".format(user)
        )
        returneduser = self.cursor.fetchall()
        email = returneduser[0]['email']
        return email

    def validate_comment(self, comment):
        valid = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(valid.search(comment) == None):
            return True
        else:
            return False

    def get_from_type_by_id(self, incidenttype, incident_id):
        self.cursor.execute(
            "SELECT * FROM incidents WHERE type = '{}' and incident_id = {}".format(
                incidenttype, incident_id)
        )
        incidents = self.cursor.fetchall()
        return incidents

    def get_by_type(self, incidenttype, user_id):
        self.cursor.execute(
            "SELECT * FROM incidents WHERE type = '{}' and created_by = {}".format(
                incidenttype, user_id)
        )
        incidents = self.cursor.fetchall()
        return incidents

    def get_by_status(self, status, user_id):
        self.cursor.execute(
            "SELECT * FROM incidents WHERE status = '{}' and created_by = {}".format(
                status, user_id)
        )
        incidents = self.cursor.fetchall()
        return incidents
