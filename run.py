import os
from app import create_app
from db_config import Db



app = create_app(os.getenv('FLASK_CONFIG'))

@app.cli.command()
def createtbl():
    """
    Create databas tables
    :return None
    """
    Db().init_app(app)
    Db().create_tables()