import sqlalchemy
import json
import os


class Database(object):
    CONFIG_FILE_NAME = ".serverless-secrets.json"

    def __init__(self):
        self.user = self.get_db_config('user')
        self.password = self.get_db_config('password')
        self.host = self.get_db_config('host')
        self.port = self.get_db_config('port')
        self.db = self.get_db_config('db')

    def get_db_config(self, setting):
        config_path = os.path.join(os.path.dirname(os.getcwd()), self.CONFIG_FILE_NAME)
        
        with open(config_path) as config:
            self.secrets = json.load(config)
        
        return self.secrets[setting]

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
