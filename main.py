from flask import Flask

# from data import db_session
# from data.Jobs import Jobs
# from data.users import User
from data.db_session import global_init, create_session
from data.users import User
import datetime

from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.Jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def Journal_of_works():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("Journal_of_works.html", jobs=jobs)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    app.run(port=8080, host='127.0.0.1', debug=True)
