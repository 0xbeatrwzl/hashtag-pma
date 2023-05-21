from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    if request.method == "GET":
        print('a')
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
