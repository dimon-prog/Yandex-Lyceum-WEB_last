from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')


class GameAddForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    picture = FileField('Иллюстрация игры', validators=[FileRequired()])
    genre = StringField('Жанр', validators=[DataRequired()])
    content = TextAreaField("Описание")
    archive = FileField('Файлы игры', validators=[FileRequired()])
    platform = StringField('Поддерживаемые платформы', validators=[DataRequired()])
    created_date = StringField("Год релиза", validators=[DataRequired()])
    submit = SubmitField('Применить')

