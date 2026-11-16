








from app.features.home import bp as home_bp
from app.features.register import bp as register_bp
from app.features.login import bp as login_bp
from app.features.logout import bp as logout_bp
from app.features.change_password import bp as change_password_bp
from app.features.reset_password import bp as reset_password_bp
from app.features.profile import bp as profile_bp


def register_all_features(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(change_password_bp)
    app.register_blueprint(reset_password_bp)
    app.register_blueprint(profile_bp)
