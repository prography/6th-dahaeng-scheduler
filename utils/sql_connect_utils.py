import sqlalchemy
import json
import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only


class Database(object):

    def __init__(self):
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)

        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.db = os.getenv("DB_NAME")

    def connect(self):
        '''Returns a connection and a metadata object'''
        # We connect with the help of the PostgreSQL URL
        # postgresql://federer:grandestslam@localhost:5432/tennis

        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(self.user, self.password, self.host, self.port, self.db)

        # The return value of create_engine() is our connection object
        con = sqlalchemy.create_engine(url, client_encoding='utf8')

        # We then bind the connection to MetaData()
        # meta = sqlalchemy.MetaData(bind=con, reflect=True)

        return con
