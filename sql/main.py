from flask import Flask
from data import db_session
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
from data.users import Users
from data.jobs import Jobs


def main():
    db_session.global_init("db/mars.db")
    # app.run()
    session = db_session.create_session()

    user = Users()
    user.surname = "Scott"
    user.name = 'Ridley'
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    session.add(user)

    user = Users()
    user.surname = "Вискотти"
    user.name = 'Стефанно'
    user.age = 31
    user.position = "подчиняемый"
    user.speciality = "research engineer"
    user.address = "module_2"
    user.email = "stevano88@mars.org"
    session.add(user)

    user = Users()
    user.surname = "Babakovich"
    user.name = 'Asja'
    user.age = 18
    user.position = "подчиняемый"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "asiii@mars.org"
    session.add(user)

    user = Users()
    user.surname = "Bibizjan"
    user.name = 'Akim'
    user.age = 33
    user.position = "подчиняемый"
    user.speciality = "research engineer"
    user.address = "module_2"
    user.email = "bibizjan1234@mars.org"
    session.add(user)

    session.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = 2
    job.start_date = datetime.datetime.now().date()
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 5
    job.collaborators = 3
    job.start_date = datetime.datetime.now().date()
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 2
    job.collaborators = 2
    job.start_date = datetime.datetime.now().date()
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 4
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 6
    job.collaborators = 3
    job.start_date = datetime.datetime.now().date()
    job.is_finished = False
    session.add(job)

    session.commit()


if __name__ == '__main__':
    main()
