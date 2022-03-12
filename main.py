import datetime

from flask import Flask, request, make_response, session, render_template
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import CSRFProtect
from werkzeug.utils import redirect

from data import db_session
from data.Job import Job
from data.db_session import global_init
from data.users import User
from forms.JobForm import JobForm
from forms.RegisterForm import RegisterForm
from forms.UserForm import LoginForm

csrf = CSRFProtect()

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
csrf.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User()
        user.email = form.email.data
        user.name = form.name.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def main():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        # if db_sess.query(User).filter(User.email == form.email.data).first():
        #     return render_template('register.html', title='Регистрация',
        #                            form=form,
        #                            message="Такой пользователь уже есть")
        if current_user.is_authenticated:
            return render_template('main.html', title='Регистрация', message="Необходимо войти")
        job = Job()
        job.team_leader = current_user
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.is_finished = form.is_finished.data
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('main.html', title='Регистрация', form=form)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    forms = JobForm()
    if forms.validate_on_submit():
        db_sess = db_session.create_session()
        if not current_user.is_authenticated:
            return redirect('/')
        job = Job()
        job.team_leader = current_user.get_id()
        job.job = forms.job.data
        job.work_size = forms.work_size.data
        job.is_finished = forms.is_finished.data
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('JobForm.html', title='Регистрация', forms=forms)


if __name__ == '__main__':
    global_init("db/db.db")
    app.run(port=8080, host='127.0.0.1')
