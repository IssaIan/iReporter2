import json
from tests.v2.base_test import BaseTest


class IncidentTests(BaseTest):

    def test_create_record(self):
        response = self.create_incident()
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Record successfully saved!')
        self.assertEqual(response.status_code, 201)

    def test_get_incident_byId(self):
        self.create_incident()
        response = self.app.get('/api/v2/redflag/1', headers = {'Authorization': 'Bearer {}'.format(self.user1_token()),
                               'content-type': 'application/json'})
        result = json.loads(response.data)
        self.assertEqual(result[0]['Message'], 'Record returned successfully')
        self.assertEqual(response.status_code, 200)

    def test_fail_getbyId(self):
        self.create_incident()
        response = self.app.get('/api/v2/incidents/100', headers = {'Authorization': 'Bearer {}'.format(self.user1_token()),
                               'content-type': 'application/json'})
        result=json.loads(response.data)
        self.assertEqual(result['Message'], 'Record not found!')
        self.assertEqual(response.status_code, 404)

    def test_fetch_all_incidents(self):
        self.create_incident()
        response=self.app.get('/api/v2/incidents', headers = {'Authorization': 'Bearer {}'.format(self.user1_token()),
                               'content-type': 'application/json'})
        result=json.loads(response.data)
        self.assertEqual(result[0]['Message'], 'Records returned successfully')
        self.assertEqual(response.status_code, 200)

    def test_update_incident_location(self):
        self.create_incident()
        response=self.app.patch('/api/v2/redflag/1/location',
                                  json=self.update_incidentlocation,
                                  headers={'Authorization': 'Bearer {}'.format(self.user1_token()),
                               'content-type': 'application/json'}
                                  )
        result = json.loads(response.data)
        self.assertEqual(result[0]['Message'], 'Updated redflag location successfully!')
        self.assertEqual(response.status_code, 200)

    def test_update_incident_description(self):
        self.create_incident()
        response=self.app.patch('/api/v2/redflag/1/comment',
                                  json=self.update_incidentcomment,
                                  headers={'Authorization': 'Bearer {}'.format(self.user1_token()),
                               'content-type': 'application/json'}
                                  )
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result[0]['Message'], 'Updated redflag comment successfully!')

    def test_updating_a_nonexistence_incident(self):
        self.create_incident()
        self.registration()
        self.login()
        response=self.app.patch('/api/v2/redflag/20/comment',
                                  json=self.update_incidentcomment,
                                  headers={'Authorization': 'Bearer {}'.format(self.user1_token()),
                                           'content-type': 'application/json'})
        self.assertEqual({'Message': 'Record not found!'}, response.get_json())

    def test_delete_incident(self):
        self.create_incident()
        response=self.app.delete('/api/v2/redflag/1', 
                                headers={'Authorization': 'Bearer {}'.format(self.user1_token()),
                                        'content-type': 'application/json'
                                        }
                                )
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Record successfully deleted!')
        self.assertEqual(response.status_code, 200)

    def test_fail_delete_incident(self):
        self.create_incident()
        response=self.app.delete('/api/v2/redflag/200',  headers={'Authorization': 'Bearer {}'.format(self.user1_token()),
                               'content-type': 'application/json'})
        self.assertEqual({'Message': 'The record you are trying to delete has not been found!',
                          }, response.get_json())

    def test_updatestatus(self):
        self.create_incident()
        response=self.app.patch('/api/v2/admin/redflag/1/statusupdate', json=self.update_incidentstatus,
                                headers={'Authorization': 'Bearer {}'.format(self.superadmintoken()),
                               'content-type': 'application/json'})
        self.assertEqual(response.status_code, 200)

    def test_normal_user_update_status(self):
        self.normal_user_create_incident()
        response=self.app.patch('/api/v2/admin/redflag/1/statusupdate', json=self.update_incidentstatus,
                                headers={'Authorization': 'Bearer {}'.format(self.user_token()),
                                'content-type' : 'application/json'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual({'Message' : 'You are not an admin!'}, response.get_json())