

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from app.models.user import User


class RegisterForm(FlaskForm):
    username = StringField(
        "Имя пользователя",
        validators=[
            DataRequired(message="Введите имя пользователя."),
            Length(min=3, max=30, message="Имя должно быть от 3 до 30 символов."),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Введите email."),
            Email(message="Введите корректный email."),
            Length(max=120),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired(message="Введите пароль."),
            Length(min=6, max=128, message="Пароль должен быть от 6 символов."),
        ],
    )
    confirm_password = PasswordField(
        "Повторите пароль",
        validators=[
            DataRequired(message="Повторите пароль."),
            EqualTo("password", message="Пароли не совпадают."),
        ],
    )
    submit = SubmitField("Зарегистрироваться")

    
    def validate_username(self, field):
        if User.find_by_username(field.data):
            raise ValidationError("Это имя уже занято.")

    def validate_email(self, field):
        if User.find_by_email(field.data):
            raise ValidationError("Пользователь с таким email уже существует.")
