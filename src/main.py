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

    tratatives = dict()
    data['valor'] = float(data['valor'])
    data['parcelas'] = int(data['parcelas'])

    if data['forma_pagamento'] == 'paypal':
        data['forma_pagamento'] = 'PL'

    elif data['forma_pagamento'] == 'pix':
        data['forma_pagamento'] = 'PX'

    elif data['forma_pagamento'] == 'cartao_credito':
        data['forma_pagamento'] = 'CC'

    else:
        data['forma_pagamento'] = 'BO'

    if data['status'] == 'aprovado':
        tratatives['acesso'] = '1'
        tratatives['mensagem'] = 'BEM-VINDO, ALUNO'
        data['status'] = 'AP'

    elif data['status'] == 'recusado':
        tratatives['acesso'] = '0'
        tratatives['mensagem'] = 'PAGAMENTO RECUSADO'
        data['status'] = 'RC'

    else:
        tratatives['acesso'] = '0'
        tratatives['mensagem'] = 'VALOR REEMBOLSADO'
        data['status'] = 'RB'

    db.insert_data(
        table='webhook',
        nome=data['nome'],
        email=data['email'],
        status_pagamento=data['status'],
        metodo_pagamento=data['forma_pagamento'],
        valor=data['valor'],
        parcelas=data['parcelas']
    )

    db.insert_data(
        table='system_tratatives',
        acesso=tratatives['acesso'],
        mensagem=tratatives['mensagem']
    )

    return 'Webhook received! Thank you.'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


# RUN

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
