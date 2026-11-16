

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required

from app.extensions import db
from app.forms.profile_form import ProfileForm

bp = Blueprint("profile", __name__)


@bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile_page():
    
    form = ProfileForm(obj=current_user)

    if form.validate_on_submit():
        current_user.username = form.username.data.strip()
        db.session.commit()
        flash("Профиль обновлён.", "success")
        return redirect(url_for("profile.profile_page"))

    return render_template("profile.html", form=form)
