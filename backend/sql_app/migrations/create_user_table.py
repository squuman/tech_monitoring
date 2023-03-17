"""
Создание таблицы пользователей
"""
from sql_app import Migration
from sql_app import Connector
from config import DATABASE


class CreateUserTableMigration(Migration):
    _connector = Connector(DATABASE['host'], DATABASE['user'], DATABASE['password'], DATABASE['database'])

    def up(self):
        self._connector.cursor.execute("CREATE TABLE users("
                                                   "id INT PRIMARY KEY AUTO_INCREMENT,"
                                                   "name VARCHAR(255),"
                                                   "password VARCHAR(255),"
                                                   "is_delete BOOLEAN DEFAULT FALSE,"
                                                   "is_admin BOOLEAN DEFAULT FALSE,"
                                                   "created_at DATETIME DEFAULT CURRENT_TIMESTAMP"
                                                   ");")

    def down(self):
        self._connector.cursor.execute("DROP TABLE IF EXISTS users")
