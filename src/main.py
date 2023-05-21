# IMPORTS

import os
import pymysql

from flask import Flask, render_template, request


# VARIABLES

MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']


# APP CONFIG

app = Flask(__name__)


# DATABASE CONFIG

connector = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    passwd=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)


# ROUTES

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.data)

    return 'Webhook received! Thank you.'


@app.route('/')
def home():
    return render_template('index.html')


# RUN

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
