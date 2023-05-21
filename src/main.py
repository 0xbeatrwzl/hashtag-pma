from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


# VARIABLES

DATABASE_URL = os.environ['DATABASE_URL']


# APP CONFIG

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

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
