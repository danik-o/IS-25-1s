

from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "Новый пароль",
        validators=[
            DataRequired(message="Введите новый пароль."),
            Length(min=8, max=128, message="Пароль должен быть от 8 символов."),
        ],
    )
    confirm_password = PasswordField(
        "Повторите новый пароль",
        validators=[
            DataRequired(message="Повторите новый пароль."),
            EqualTo("password", message="Пароли не совпадают."),
        ],
    )
    submit = SubmitField("Сохранить новый пароль")
