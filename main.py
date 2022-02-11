import os.path

from flask import Flask
from flask import render_template

app = Flask(__name__)

static = os.path.join('static')


# @app.route('/')
# def start():
#     return "Миссия Колонизация Марса"


@app.route('/<title>')
@app.route('/index/<title>')
def image_mars(title: str):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof: str):
    flag = True if "инженер" in prof.split() or "строитель" in prof.split() else False
    text = ""
    url_photo = os.path.join(static, 'img', 'mars.png')
    if flag:
        text = "Инженерные тренажеры"
        url_photo = os.path.join(static, "img", "1.png")
    else:
        text = "Научные симуляторы"
        url_photo = os.path.join(static, "img", "2.png")
    return render_template('training.html', text=text, url_photo=url_photo, flag=flag)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
