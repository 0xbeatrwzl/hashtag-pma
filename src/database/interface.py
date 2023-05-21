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
            values.append(values)

        query = (f'INSERT INTO {table} ({columns})'
                 f'VALUES ({values})')

        self.cursor.execute(query)

    def load_data(self, table):
        query = f'SELECT * FROM {table};'
        response = self.cursor.execute(query)

        return response
