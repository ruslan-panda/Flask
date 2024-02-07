from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def page():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title> ЧТО ВЫ ТУТ ХОТИТЕ УВИДЕТЬ</title>
                      </head>
                      <body>
                        <h5>Человечество вырастает из детства.</h5>
                        <h5>Человечеству мала одна планета.</h5>
                        <h5>Мы сделаем обитаемыми безжизненные пока планеты.</h5>
                        <h5>И начнем с Марса!</h5>
                        <h5>Присоединяйся!</h5>
                      </body>
                    </html>"""


@app.route('/image_mars')
def mars():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">'
                            <h5>Вот она какая, красная планета</h5>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
