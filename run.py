import os
from app import create_app
from db_config import Db

app = create_app(os.getenv('FLASK_CONFIG'))

if __name__ == '__main__':
    app.run(DEBUG = True)


