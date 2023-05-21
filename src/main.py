from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    print(request)
    return 'Webhook received! Thank you.'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
