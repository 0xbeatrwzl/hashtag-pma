# IMPORTS

from database.connector import Connector


# INTERFACE CLASS

class Database:
    def __init__(self):
        self.cursor = Connector.cursor()

    def insert_data(self, table, **kwargs):
        columns = []
        values = []
        for column, value in kwargs.items():
            columns.append(column)
            values.append(value)

        columns = str(columns).replace("'", "")
        query = f'INSERT INTO {table} ({columns}) VALUES ({values});'.replace('[', '').replace(']', '')

        self.cursor.execute(query)

        Connector.commit()

    def load_data(self, table):
        query = f'SELECT * FROM {table};'
        response = self.cursor.execute(query)

        return response
