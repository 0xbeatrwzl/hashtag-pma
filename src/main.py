# IMPORTS

import os

from flask import Flask, render_template, request
from database.connector import connector

# APP CONFIG

app = Flask(__name__)

print(connector.cursor().execute('SELECT * FROM webhooks'))


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
