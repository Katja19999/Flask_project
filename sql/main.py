from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user

from data import db_session
from data.jobs import Jobs
from data.login_form import LoginForm
from data.register_form import RegisterForm
from data.users import User
from flask_restful import Api
from sql.api_v2.jobs_api_v2 import JobsResource, JobsListResource

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

api_version2 = Api(app)





api_version2.add_resource(JobsResource, '/api/v2/jobs/<int:job_id>')
api_version2.add_resource(JobsListResource, '/api/v2/jobs')

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login_2.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.password.data != form.repeat_password.data:
        return render_template('register.html', title='Регистрация', message='Пароли не совпадают', form=form)
    session = db_session.create_session()
    if form.validate_on_submit():
        user = session.query(User).filter(User.email == form.email.data).first()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', message='Такой пользователь уже есть',
                                   form=form)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация пользователя', form=form)


def main():
    db_session.global_init('db/mars.db')
    app.run()


if __name__ == '__main__':
    main()
