import flask
from flask import jsonify

from . import db_session
from .Job import Job

blueprint = flask.Blueprint(
    'Job_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(Job).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    'id', 'team_leader', 'job', 'work_size', 'start_date', 'collaborators',
                    'is_finished'))
                    for item in news]
        }
    )
