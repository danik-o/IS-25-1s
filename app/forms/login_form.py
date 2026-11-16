

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Введите email."),
            Email(message="Введите корректный email."),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired(message="Введите пароль.")],
    )
    remember = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")
