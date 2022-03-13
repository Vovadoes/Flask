import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from data import db_session
from .users import User
from .users import association_table


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"),
                                    nullable=True)
    # team_leader = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    # position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True, default=datetime.datetime.now)
    # end_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    collaborators = orm.relationship('User', secondary=association_table, back_populates='jobs')
    # collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    def get_team_leader(self):
        db_sess = db_session.create_session()
        return db_sess.query(User).filter(User.id == self.team_leader).first()

    def get_users_names(self):
        return ', '.join([f'{collaborator.name} {collaborator.surname}' for collaborator in
                           self.collaborators])
