from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegistryForm(FlaskForm):
    username = StringField(' Введите логин', validators=[DataRequired()])
    email = StringField(' Введите email', validators=[Email()])
    password = PasswordField(' Введите пароль', validators=[Length(6)])
    password2 = PasswordField(' Введите пароль еще раз', validators=[DataRequired()])

    submit = SubmitField('Зарегистрироваться')
