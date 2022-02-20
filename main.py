import os.path

from flask import Flask
from flask import render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

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


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ['Первая профессия', 'Вторая профессия', 'Третья профессия']
    h2_text = ''
    return render_template('list_prof.html', professions=professions, h2_text=h2_text, tag=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    d = {'title': 'Mars One',
              'surname': 'V',
              'name': 'D',
              'education': 'среднее',
              'profession': 'радист',
              'sex': 'male',
              'motivation': 'Пожить пожить жить жить',
              'ready': 'True'}
    return render_template('auto_answer.html', title=d["title"], surname=d["surname"],
                           name=d["name"],
                           education=d["education"], profession=d["profession"], sex=d["sex"],
                           motivation=d["motivation"], ready=d["ready"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
