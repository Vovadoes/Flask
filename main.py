import os.path

from flask import Flask
from flask import render_template

app = Flask(__name__)

static = os.path.join('static')


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


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


@app.route('/promotion_image')
def promotion_image():
    url_photo = os.path.join(static, 'img', 'mars.png')
    texts = ["Мы сделаем обитаемыми безжизненые планеты!", "И начнем марса!", 'Присоединяйся']
    return render_template('promotion_image.html', title="Привет, Марс!", h1_text="Жди нас, Марс!",
                           url_photo=url_photo, texts=texts)


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut_selection.html')


@app.route('/choice/<planet_name>')
def planet_name(planet_name: str):
    h1_text = f"Моё предложение {planet_name}"
    texts = [f'Это планета {planet_name}', f"Наоборот {planet_name[::-1]}"]
    return render_template('choice.html', h1_text=h1_text, texts=texts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
