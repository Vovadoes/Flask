from flask import Flask
from data import db_session
from data.Jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()

    user1 = User()
    user1.name = 'Ridley'
    user1.surname = 'Scott'
    user1.age = 21
    user1.position = 'captain'
    user1.speciality = 'research engineer'
    user1.address = 'module_1'
    user1.email = 'scott_chief@mars.org'
    db_sess.add(user1)

    user2 = User()
    user2.name = 'vova'
    user2.surname = 'Scott'
    user2.age =15
    user2.position = 'user'
    user2.speciality = 'research engineer'
    user2.address = 'module_2'
    user2.email = 'vova@mars.org'
    db_sess.add(user2)

    user3 = User()
    user3.name = 'danila'
    user3.surname = 'Scott'
    user3.age = 15
    user3.position = 'user'
    user3.speciality = 'research engineer'
    user3.address = 'module_3'
    user3.email = 'danila@mars.org'
    db_sess.add(user3)

    user4 = User()
    user4.name = 'dima'
    user4.surname = 'Scott'
    user4.age = 15
    user4.position = 'user'
    user4.speciality = 'research engineer'
    user4.address = 'module_4'
    user4.email = 'dima@mars.org'
    db_sess.add(user4)

    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
