from flask_restful import Resource
import flask
from sql.data import db_session


class JobsResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return flask.jsonify({'jobs': ([item.to_dict(
            only=('id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
            for item in jobs])})

    def post(self):
        pass


class JobsListResource(Resource):
    def get(self):
        pass
