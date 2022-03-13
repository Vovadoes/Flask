from flask_wtf import FlaskForm
import wtforms.fields
from wtforms.validators import DataRequired


class JobFormValidate(FlaskForm):
    job = wtforms.StringField('Название', validators=[DataRequired()])
    work_size = wtforms.IntegerField('work_size', validators=[DataRequired()])
    # is_finished = wtforms.BooleanField('is_finished', validators=[DataRequired()])
    # submit = wtforms.SubmitField('Войти')


class JobFormNoValidate(FlaskForm):
    is_finished = wtforms.BooleanField('is_finished', validators=[DataRequired()])
    submit = wtforms.SubmitField('Войти')
