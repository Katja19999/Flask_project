from flask import Flask
from data import db_session

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


if __name__ == '__main__':
    main()
