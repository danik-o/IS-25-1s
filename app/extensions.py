



from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()


login_manager = LoginManager()


csrf = CSRFProtect()



login_manager.login_view = "login.login_page"
login_manager.login_message = "Войдите, чтобы открыть эту страницу."
login_manager.login_message_category = "warning"
