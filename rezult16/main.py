from flask import Flask

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
