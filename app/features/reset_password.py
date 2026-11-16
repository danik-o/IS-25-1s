







from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user

from app.extensions import db
from app.models.user import User
from app.forms.reset_request_form import ResetRequestForm
from app.forms.reset_password_form import ResetPasswordForm

bp = Blueprint("reset_password", __name__)


@bp.route("/reset-password", methods=["GET", "POST"])
def request_reset_page():
    if current_user.is_authenticated:
        return redirect(url_for("change_password.change_password_page"))

    form = ResetRequestForm()

    if form.validate_on_submit():
        user = User.find_by_email(form.email.data)
        if user:
            token = user.get_reset_token()
            link = url_for("reset_password.reset_page", token=token, _external=True)
            
            print(f"\n=== Ссылка для сброса пароля ({user.email}) ===\n{link}\n")

        
        flash(
            "Если такой email зарегистрирован, ссылка для сброса пароля отправлена. "
            "(Учебная версия: ссылку смотрите в терминале.)",
            "info",
        )
        return redirect(url_for("login.login_page"))

    return render_template("auth/reset_request.html", form=form)


@bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_page(token):
    if current_user.is_authenticated:
        return redirect(url_for("change_password.change_password_page"))

    user = User.verify_reset_token(token)
    if user is None:
        flash("Ссылка недействительна или устарела. Запросите новую.", "danger")
        return redirect(url_for("reset_password.request_reset_page"))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Пароль изменён. Теперь можно войти.", "success")
        return redirect(url_for("login.login_page"))

    return render_template("auth/reset_password.html", form=form)
