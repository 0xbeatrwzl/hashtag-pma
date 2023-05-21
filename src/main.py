from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.json())


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
