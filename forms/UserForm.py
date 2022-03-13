from flask_wtf import FlaskForm
import wtforms.fields
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = wtforms.EmailField('Почта', validators=[DataRequired()])
    age = wtforms.IntegerField("Возраст", validators=[DataRequired()])
    position = wtforms.StringField("position", validators=[DataRequired()])
    speciality = wtforms.StringField("Специальность", validators=[DataRequired()])
    address = wtforms.StringField("Адрес", validators=[DataRequired()])
    password = wtforms.PasswordField('Пароль', validators=[DataRequired()])
    remember_me = wtforms.BooleanField('Запомнить меня', )
    submit = wtforms.SubmitField('Войти')
