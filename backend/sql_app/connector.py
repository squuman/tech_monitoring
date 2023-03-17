"""
File connector for database
"""
import pymysql


class Connector:
    host: str
    user: str
    password: str
    database: str

    connector = None
    cursor = None

    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.connector = pymysql.connect(host=self.host, user=self.user,
                                         password=self.password, database=self.database)
        self.cursor = self.connector.cursor()

    def __repr__(self):
        return self.connector
