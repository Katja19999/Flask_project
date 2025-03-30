from flask_restful import Resource
import flask
from sql.data import db_session
from sql.data.jobs import Jobs


class JobsResource(Resource):
    def get(self, job_id):
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return flask.jsonify({'jobs': ([job.to_dict(
            only=('id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))])})

    def post(self):
        pass


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return flask.jsonify({'jobs': ([item.to_dict(
            only=('id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
            for item in jobs])})