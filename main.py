from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<lst>')
def index(lst):
    professions = ['инженер', 'строитель', 'пилот', 'врач']
    return render_template('list_prof.html', list=lst, professions=professions,
                           title='Список профессий')


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        "title": "Анкета",
        "surname": "Горбенко",
        "name": "Екатерина",
        "education": "Среднее",
        "profession": "Ученик",
        "sex": "Женский",
        "motivation": "Нет",
        "ready": True
    }
    return render_template('answer.html', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
