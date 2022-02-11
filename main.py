import os.path

from flask import Flask
from flask import render_template

app = Flask(__name__)

static = os.path.join('static')


# @app.route('/')
# def start():
#     return "Миссия Колонизация Марса"


@app.route('/')
@app.route('/index')
def image_mars():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
