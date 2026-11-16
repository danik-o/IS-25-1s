



from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, logout_user

bp = Blueprint("logout", __name__)


@bp.route("/logout", methods=["POST"])
@login_required
def logout_action():
    logout_user()
    flash("Вы вышли из аккаунта.", "info")
    return redirect(url_for("home.index"))
