import sqlalchemy
import os
from dotenv import load_dotenv


ENV_PATH = os.path.dirname(os.getcwd()) + "/.env"
load_dotenv(dotenv_path=ENV_PATH)

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB = os.getenv("DB_NAME")


def connect():
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis

    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(USER, PASSWORD, HOST, PORT, DB)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    # meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con
