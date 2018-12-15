# iReporter2

[![Build Status](https://travis-ci.org/IssaIan/iReporter2.svg?branch=develop)](https://travis-ci.org/IssaIan/iReporter2)
[![Coverage Status](https://coveralls.io/repos/github/IssaIan/iReporter2/badge.svg?branch=develop)](https://coveralls.io/github/IssaIan/iReporter2?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9b7374eb098e48c5a7d5c77bb123a6b1)](https://app.codacy.com/app/IssaIan/iReporter2?utm_source=github.com&utm_medium=referral&utm_content=IssaIan/iReporter2&utm_campaign=Badge_Grade_Settings)
[![Maintainability](https://api.codeclimate.com/v1/badges/2df90d509788fc828151/maintainability)](https://codeclimate.com/github/IssaIan/iReporter2/maintainability)

This is a version 2 of the iReporter app which uses databases.
iReporter is a digital platform for citizens to report corruption cases to relevant authorities. Users can also report on things that need government intervention.

Click [HERE](https://ireporter7.docs.apiary.io/#) to view the API documentation

Click [HERE](https://issaireporterv2.herokuapp.com/) to view the app on HEROKU

## Installation

To install and run the project locally:

    - Clone the repo: git clone https://github.com/IssaIan/iReporter2.git
    - cd into iReporter2/
    - virtualenv -p python3 env
    - source env/bin/activate
    - pip install -r requirements.txt
    - export FLASK_APP=run.py
    - flask run

## Api Endpoints

| **HTTP METHOD** | **URI**                             | **ACTION**                                                                     |
|-----------------|-------------------------------------|------------------------------------------------------------------------|
|  **GET**        |  `/incidents`                                           | fetch all incident records                                                    |
|  **POST**       |  `/incidents`                                           | create incident record                                                         |
| **DELETE, GET** |  `/<incidenttype>/<int:incident_id>`                    | get and delete incident records with given `incidenttype` and `incident_id` |
| **PATCH**       | `/<incidenttype>/<int:incident_id>`                     | update incident records with given `incidenttype` and `incident_id`            |
|  **GET**        |  `/incidenttype/<int:incident_id>`                      | get list of all incidents, create incident                                     |
|  **POST**       |  `auth/signup`                                          | registers a new user                                                           |
|  **GET**        |  `/auth/signup`                                         | fetch all users(admin only)                                                    |
| **POST**        | `/auth/login`                                           | login in a user                                                                |
| **PATCH**       | `/admin//<incidenttype>/<int:incident_id>/statusupdate` | admin updates incident's status                                                |

### Author : Issa