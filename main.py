from flask import Flask, render_template, url_for

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


@app.route('/choice/<planet_name>')
def choice(planet_name):
    spisok = [
        planet_name,
        'На неё много необходимых ресурсов;',

        'На ней есть вода и атмосфера;',

        'На ней есть небольшое магнитное поле;',

        'Наконец, она просто красива!;',

    ]
    url_pic = url_for('static', filename='img/MARS.png')
    url_style = url_for('static', filename='css/style.css')
    return """<!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>


            <title>Колонизация</title>
        </head>
        <body>
        <h1>Моё предложение: {}</h1>
        <h3>Эта планета близка к Земле:</h3>
        <div class="alert alert-primary" role="alert">
          <h3>{}</h3>
        </div>
        <div class="alert alert-secondary" role="alert">
          <h3>{}</h3>
        </div>
        <div class="alert alert-success" role="alert">
          <h3>{}</h3>
        </div>
        <div class="alert alert-danger" role="alert">
          <h3>{}</h3>
        </div>
        </body>
        </html>""".format(*spisok)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    spisok = [
        f'Претендента на участие в миссии {nickname}:',
        f'Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}!',

        'Желаем удачи!',

    ]
    return """<!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>


            <title>Результаты</title>
        </head>
        <body>
        <h1>Результаты отбора</h1>
        <h3>{}</h3>
        <div class="alert alert-success" role="alert">
          <h3>{}</h3>
        </div>
        <div class="alert alert-secondary" role="alert">
          <h3>{}</h3>
        </div>
        </body>
        </html>""".format(*spisok)


@app.route('/gallery')
def gallery():
    images = [url_for('static', filename='img/mars.webp'),
              url_for('static', filename='img/mars2.jpg'),
              url_for('static', filename='img/mars3.jpg')]
    return """<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <title>Галерея Марса</title>
</head>
<body>
    <h1>Пейзажи Марса</h1>
    <!-- Carousel wrapper -->
    <div id="carouselBasicExample" class="carousel slide carousel-fade" data-bs-ride="carousel">
        <!-- Indicators -->
        <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselBasicExample" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselBasicExample" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselBasicExample" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>

        <!-- Inner -->
        <div class="carousel-inner">
            <!-- Single item -->
            <div class="carousel-item active">
                <img src="{}" class="d-block w-100" alt="Sunset Over the City">
            </div>
            <!-- Single item -->
            <div class="carousel-item">
                <img src="{}" class="d-block w-100" alt="Canyon at Night">
            </div>
            <!-- Single item -->
            <div class="carousel-item">
                <img src="{}" class="d-block w-100" alt="Cliff Above a Stormy Sea">
            </div>
        </div>

        <!-- Controls -->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselBasicExample" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselBasicExample" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>
</body>
</html>
    """.format(*images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
