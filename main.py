import json
import os
from random import choice

from flask import Flask, render_template, url_for, redirect
from werkzeug.utils import secure_filename

from loginform import LoginForm
from imageform import ImageForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['IMAGES'] = 1


@app.route('/')
@app.route('/index')
def index():
    name = "И на Марсе будут яблони цвести!"
    return render_template('index.html', title='Индекс страница',
                           mission=name)


@app.route('/training/<prof>')
def prof_training(prof):
    prof = prof.lower()
    if "инженер" in prof or "строитель" in prof:
        profession = "Инженерные тренажёры"
        image = "ing_schip..jpg"
    else:
        profession = "Научные симуляторы"
        image = "scn_schip.jpg"
    return render_template('training.html',
                           profession=profession,
                           image=url_for('static', filename='img/' + image))


@app.route('/list_prof/<type_of_list>')
def list_prof(type_of_list):
    return render_template('list.html',
                           type_of_list=type_of_list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    with open('templates/dict_answer.json', "rt", encoding="utf8") as f:
        info = json.load(f)
    return render_template('auto_answer.html',
                           info=info)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('index')
    return render_template('login.html',
                           form=form)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', astronauts=astronauts)


@app.route('/table_param/<gender>/<int:age>')
def table_param(gender: str, age: int):
    return render_template('table_param.html',
                           age=age,
                           gender=1 if gender == "male" else 0,
                           image=url_for('static', filename=f'img/alien_{1 if age > 21 else 2}.jpg'))


@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    form = ImageForm()
    if form.validate_on_submit():
        i = form.image.data
        filename = secure_filename(i.filename)
        with open('static/img/carousel/' + filename, 'wb') as f:
            f.write(i.read())
        app.config['IMAGES'] += 1
        return redirect('carousel')
    images = os.listdir('static/img/carousel/')
    return render_template('carousel.html',
                           images=[url_for('static', filename='img/carousel/' + image) for image in images],
                           form=form)


@app.route('/member')
def member():
    with open('templates/members.json', "r", encoding="utf-8") as f:
        members = json.load(f)
    person = choice(members)
    return render_template('member.html', user=person)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
