import flask
from flask import jsonify, request

from . import db_session
from .Job import Job
from .users import User

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


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    job = Job()

    if request.json['collaborators'] is list:
        for id in request.json['collaborators']:
            if db_sess.query(User).filter(User.id == id).first() is None:
                print(f'User with ID {id} not detected')
                return jsonify({'error': 'Bad request'})

        job.collaborators = request.json['collaborators']

    if 'id' in request.json:
        if db_sess.query(Job).filter(Job.id == request.json['id']).first() is not None:
            return jsonify({'error': 'Id already exists.'})
        else:
            job.id = request.json['id']

    job.team_leader = request.json['team_leader']
    job.job = request.json['job']
    job.work_size = request.json['work_size']
    job.is_finished = request.json['is_finished']

    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})
