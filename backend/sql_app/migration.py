"""
Describe migration class
"""
from sql_app import Connector


class Migration:
    _connector: Connector

    def up(self):
        pass

    def down(self):
        pass
