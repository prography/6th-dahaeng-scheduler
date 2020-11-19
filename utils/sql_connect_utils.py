import sqlalchemy
import json
import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only


def connect():
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis

    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    # meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con
