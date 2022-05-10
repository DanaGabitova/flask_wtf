from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, FileField


class ImageForm(FlaskForm):
    image = FileField('Новое фото', validators=[DataRequired()])
    submit = SubmitField('Добавить')
