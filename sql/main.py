from flask import Flask, render_template, redirect
from data import db_session
import datetime
import sqlalchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
from data.jobs import Jobs
from data.login_form import LoginForm

@app.route('/')
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("index.html", jobs=jobs)

@app.route('/login', method=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_1.html', title='Авторизация', form=form)

def main():
    db_session.global_init('db/mars.db')
    app.run()

if __name__ == '__main__':
    main()
