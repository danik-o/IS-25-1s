



from datetime import datetime, timezone

from flask import current_app
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    

    def set_password(self, password):
        """Превращает пароль в хеш и сохраняет в объекте."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Проверяет, подходит ли введённый пароль к сохранённому хешу."""
        return check_password_hash(self.password_hash, password)

    

    @staticmethod
    def find_by_email(email):
        """Ищет пользователя по email (без учёта регистра). Если нет — None."""
        return User.query.filter(db.func.lower(User.email) == email.strip().lower()).first()

    @staticmethod
    def find_by_username(username):
        """Ищет пользователя по имени (без учёта регистра). Если нет — None."""
        return User.query.filter(
            db.func.lower(User.username) == username.strip().lower()
        ).first()

    

    def get_reset_token(self):
        """Создаёт подписанный токен для ссылки «сбросить пароль».
        В токен кладём кусочек хеша пароля: после смены пароля
        старая ссылка автоматически перестаёт работать."""
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        return serializer.dumps(
            {"user_id": self.id, "ph": self.password_hash[-10:]},
            salt="reset-password",
        )

    @staticmethod
    def verify_reset_token(token, max_age=3600):
        """Проверяет токен (по умолчанию он живёт 1 час).
        Возвращает пользователя или None, если токен неверный/устарел."""
        serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        try:
            data = serializer.loads(token, salt="reset-password", max_age=max_age)
        except Exception:
            return None
        user = db.session.get(User, data.get("user_id"))
        if user is None or user.password_hash[-10:] != data.get("ph"):
            return None
        return user


@login_manager.user_loader
def load_user(user_id):
    """Flask-Login вызывает эту функцию, чтобы по id из сессии
    достать пользователя из базы."""
    return db.session.get(User, int(user_id))
