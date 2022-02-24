import os.path

from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from os.path import join, dirname, realpath
from flask import render_template

# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads')

# UPLOAD_FOLDER = '/static/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPEG', 'ifif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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


@app.route('/distribution')
def distribution():
    people = ["Дмитрий", 'Владимир', "Даниил"]
    return render_template('distribution.html', people=people)


@app.route('/table/<string:gender>/<int:age>')
def table(gender: str, age: int):
    photo = ''
    if age >= 18:
        photo = url_for('static', filename='img/3.png')
    else:
        photo = url_for('static', filename='img/4.png')

    r = 255
    g = 255
    b = 255
    if gender == 'male':
        b = min(255 * age / 70, 255)
    elif gender == 'female':
        r = min(255 * age / 70, 255)
    r, g, b = map(round, (r, g, b))
    color = '%02x%02x%02x' % (r, g, b)
    return render_template('table.html', url=photo, color=color)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/gallery/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', name=filename))
    else:
        lst = []
        for name in os.listdir(app.config['UPLOAD_FOLDER']):
            filename, file_extension = os.path.splitext(join(app.config['UPLOAD_FOLDER'], name))
            file_extension = file_extension[1::]
            if file_extension in ALLOWED_EXTENSIONS:
                lst.append(url_for('static', filename=f'uploads/{name}'))
        print(lst)
        return render_template('gallery.html', photos=lst)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
