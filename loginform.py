from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astronaut_id = StringField("ID астронавта", validators=[DataRequired()])
    astronaut_pass = PasswordField("Пароль астронавта", validators=[DataRequired()])

    capitan_id = StringField("ID капитана", validators=[DataRequired()])
    capitan_token = PasswordField("Пароль капитана", validators=[DataRequired()])

    submit = SubmitField('Войти')
