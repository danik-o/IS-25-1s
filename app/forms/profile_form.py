

from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models.user import User


class ProfileForm(FlaskForm):
    username = StringField(
        "Имя пользователя",
        validators=[
            DataRequired(message="Введите имя пользователя."),
            Length(min=3, max=30, message="Имя должно быть от 3 до 30 символов."),
        ],
    )
    submit = SubmitField("Сохранить")

    def validate_username(self, field):
        existing = User.find_by_username(field.data)
        
        if existing and existing.id != current_user.id:
            raise ValidationError("Это имя уже занято.")
