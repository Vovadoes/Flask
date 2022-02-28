from flask import Flask

# from data import db_session
# from data.Jobs import Jobs
# from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

global_init("db/blogs.db")
db_sess = create_session()

for user in db_sess.query(User).all():
    print(user.__repr__())
