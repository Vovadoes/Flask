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


@blueprint.route('/api/jobs/<int:job_id>')
def get_job(job_id: int):
    db_sess = db_session.create_session()
    job = db_sess.query(Job).filter(Job.id == job_id).first()

    if job is None:
        return jsonify(
            {
                'job': None
            }
        )
    else:
        return jsonify(
            {
                'job':
                    job.to_dict(only=(
                        'id', 'team_leader', 'job', 'work_size', 'start_date', 'collaborators',
                        'is_finished'))
            }
        )


@blueprint.route('/api/jobs/<string:job_id>')
def get_job_string(job_id: str):
    return jsonify(
        {
            'job': None
        }
    )
