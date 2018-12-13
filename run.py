import os
from app import create_app
from db_config import Db
from app.api.v2.models.usermodels import UserModels

app = create_app(os.getenv('FLASK_CONFIG'))

with app.app_context():
    Db().init_app(app)
    Db().create_tables()
    UserModels().create_admin()
    
if __name__ == '__main__':
    app.run(DEBUG=True)