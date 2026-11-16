

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from app.extensions import db
from app.forms.change_password_form import ChangePasswordForm

bp = Blueprint("change_password", __name__)


@bp.route("/change-password", methods=["GET", "POST"])
@login_required   
def change_password_page():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        
        if not current_user.check_password(form.old_password.data):
            flash("Текущий пароль указан неверно.", "danger")
            return render_template("auth/change_password.html", form=form)

        current_user.set_password(form.new_password.data)
        db.session.commit()

        flash("Пароль успешно изменён.", "success")
        return redirect(url_for("profile.profile_page"))

    return render_template("auth/change_password.html", form=form)
