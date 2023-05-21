# IMPORTS

import os
import ast

from flask import Flask, render_template, request
from database.interface import Database

# APP CONFIG

app = Flask(__name__)
db = Database()


# ROUTES

@app.route('/webhook', methods=['POST'])
def webhook():
    received_data = str(request.data).replace('b\'', '').replace('\'', '')
    data = ast.literal_eval(received_data)

    data['valor'] = float(data['valor'])
    data['forma_pagamento'] = 'TESTE'

    if data['status'] == 'aprovado':
        data['status'] = 'AP'
    elif data['status'] == 'reprovado':
        data['status'] = 'RP'
    else:
        data['status'] = 'RB'

    db.insert_data(
        table='webhooks',
        nome=data['nome'],
        email=data['email'],
        status_pagamento=data['status'],
        metodo_pagamento=data['forma_pagamento'],
        valor=data['valor']
    )

    return 'Webhook received! Thank you.'


@app.route('/')
def home():
    return render_template('index.html')


# RUN

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
