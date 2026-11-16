

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class ResetRequestForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Введите email."),
            Email(message="Введите корректный email."),
        ],
    )
    submit = SubmitField("Получить ссылку для сброса")
