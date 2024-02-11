from flask import Flask, url_for, render_template
from requests import request

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


@app.route('/promotion_image')
def prom_img():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" 
                            alt=здесь должна была быть картинка, но не нашлась>
                            <div class="alert alert-dark" role="alert">
                            Человечество вырастает из детства.                           
                            </div>
                            <div class="alert alert-success" role="alert">
                            Человечеству мала одна планета.
                            </div>
                           <div class="alert alert-secondary" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-warning" role="alert">
                            И начнем с Марса!
                            </div>
                            <div class="alert alert-danger" role="alert">
                            Присоединяйся!
                            </div>
                          </body>
                        </html>"""


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div align="center">
                                <h2>Анкета Претендента</h2>
                                <h4>на участие  миссии</h4>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="text" aria-describedby="textHelp" placeholder="Введите фамилию"text">
                                    <input type="text" class="form-control" id="text" placeholder="Введите имя" name="text">
                                    <label for="classSelect"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">

                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Дошкольное</option>
                                          <option>Начальное</option>
                                          <option>Чуть выше начального</option>
                                          <option>Среднее</option>
                                          <option>Выше среднего</option>
                                          <option>Высшее</option>
                                        </select>
                                        <label for="classSelect">Какие у Вас профессии</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Инженер-исследователь
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Пилот
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Строитель
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Экзобиолог
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Врач
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male">
                                        <label class="form-check-label" for="male">
                                        Инженер по терраформированию
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Климатолог
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Специалист по радиационной защите
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Астрогеолог, гляциолог
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Инженер жизнеобеспечения
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Метеоролог
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Оператор марсохода
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Киберинженер
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Штурман
                                        </label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" name="sex" id="male" value="male" >
                                        <label class="form-check-label" for="male">
                                        Пилот дронов
                                        </label>
                                    </div> 
                                <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="lam">
                                          <label class="form-check-label" for="female">
                                            Ламинат
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="par">
                                          <label class="form-check-label" for="female">
                                            Паркет
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                            </div>
                          </body>
                        </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
