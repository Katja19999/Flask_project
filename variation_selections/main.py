from flask import Flask, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
