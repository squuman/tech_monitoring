"""
Создание таблицы продуктов пользователя
"""
from sql_app import Migration
from sql_app import Connector
from config import DATABASE


class CreateUsersProductsTable(Migration):
    _connector = Connector(DATABASE['host'], DATABASE['user'], DATABASE['password'], DATABASE['database'])

    def up(self):
        self._connector.cursor.execute("CREATE TABLE users_products("
                                       "id INT PRIMARY KEY AUTO_INCREMENT,"
                                       "user_id INT,"
                                       "product_id INT,"
                                       "FOREIGN KEY (user_id) REFERENCES users (id),"
                                       "FOREIGN KEY (product_id) REFERENCES products (id),"
                                       "created_at DATETIME DEFAULT CURRENT_TIMESTAMP"
                                       ");")

    def down(self):
        self._connector.cursor.execute("DROP TABLE IF EXISTS users_products")
