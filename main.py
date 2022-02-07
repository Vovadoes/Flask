import os.path

from flask import Flask
from flask import render_template

app = Flask(__name__)

static = os.path.join('static')


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


# @app.route('/index')
# def index():
#     return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
           'Присоединяйся!']
    return '\n'.join([f"<p>{i}</p>" for i in lst])


@app.route('/image_mars')
def image_mars():
    url_photo = os.path.join(static, 'img', 'mars.png')
    return render_template('image_mars.html', title="Привет, Марс!", h1_text="Жди нас, Марс!",
                           text="Вот она какая, красная планета", url_photo=url_photo)


# @app.route('/')
# @app.route('/index')
# def index():
#     user = "Ученик Яндекс.Лицея"
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
