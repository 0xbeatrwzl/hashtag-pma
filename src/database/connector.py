# IMPORTS

import pymysql
import os


# VARIABLES

MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_PORT = os.environ['MYSQL_PORT']


# CONNECTOR CLASS

Connector = pymysql.connect(
    host=MYSQL_HOST,
    port=int(MYSQL_PORT),
    user=MYSQL_USER,
    passwd=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
