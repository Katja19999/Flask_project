from flask import Flask, render_template, redirect
from flask_login import login_user
# from data.jobs import Jobs
from data.login_form import LoginForm
from flask_login import LoginManager
from data import db_session
import datetime
import sqlalchemy
from data.users import User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    session = db_session.create_session()
    # jobs = session.query(Jobs).all()
    # return render_template("index.html", jobs=jobs)

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

def main():
    db_session.global_init('db/mars.db')
    app.run()

if __name__ == '__main__':
    main()
