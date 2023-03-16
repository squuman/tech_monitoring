"""
File connector for database
"""
import pymysql


class Connector:
    host: str
    user: str
    password: str
    database: str

    connector: object

    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.connector = pymysql.connect(host=self.host, user=self.user,
                                         password=self.password, database=self.database)

        # шо ты там угараешь? скинь ей дикпик
