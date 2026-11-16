



from flask import Flask

from config import Config
from app.extensions import db, login_manager, csrf
from app.features import register_all_features


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    
    from app import models  

    
    register_all_features(app)

    
    
    with app.app_context():
        db.create_all()

    return app
