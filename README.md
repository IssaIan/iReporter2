# iReporter2
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9b7374eb098e48c5a7d5c77bb123a6b1)](https://app.codacy.com/app/IssaIan/iReporter2?utm_source=github.com&utm_medium=referral&utm_content=IssaIan/iReporter2&utm_campaign=Badge_Grade_Settings)
[![Build Status](https://travis-ci.org/IssaIan/iReporter2.svg?branch=develop)](https://travis-ci.org/IssaIan/iReporter2)
[![Coverage Status](https://coveralls.io/repos/github/IssaIan/iReporter2/badge.svg?branch=develop)](https://coveralls.io/github/IssaIan/iReporter2?branch=develop)


This is a version 2 of the iReporter app which uses databases.
iReporter is a digital platform for citizens to report corruption cases to relevant authorities. Users can also report on things that need government intervention.

## Installation
To install and run the project locally:

    Clone the repo git clone https://github.com/IssaIan/iReporter2.git
    cd into iReporter2/
    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt
    export FLASK_APP=run.py
    flask run

## Api Endpoints

1. Create an incident: /api/v1/incidents
2. Edit a specific incident comment/description: /api/v1/incident_id/descrition
3. Edit a specific incident location: /api/v1/incident_id/location
4. Create a user: /api/v1/users
5. Get or update a specific user: /api/v1/users/user_id
