# IMPORTS

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os


# VARIABLES

DATABASE_URL = os.environ['DATABASE_URL']


# APP CONFIG

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL


# DATABASE CONFIG

database = SQLAlchemy()

database.init_app(app)


# ROUTES

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.data)
    return 'Webhook received! Thank you.'


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
