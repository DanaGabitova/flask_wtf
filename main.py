from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
