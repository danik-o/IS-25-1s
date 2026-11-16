

from urllib.parse import urlparse

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user

from app.models.user import User
from app.forms.login_form import LoginForm

bp = Blueprint("login", __name__)


def _is_safe_redirect(target):
    """Разрешаем перенаправление только на страницы нашего же сайта.
    Это защита от ссылок вида /login?next=https://чужой-сайт.com"""
    if not target:
        return False
    parsed = urlparse(target)
    return (
        target.startswith("/")
        and not target.startswith("//")
        and "\\" not in target
        and not parsed.netloc
        and not parsed.scheme
    )


@bp.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.find_by_email(form.email.data)

        
        
        if user is None or not user.check_password(form.password.data):
            flash("Неверный email или пароль.", "danger")
            return render_template("auth/login.html", form=form)

        login_user(user, remember=form.remember.data)
        flash("Вы вошли в аккаунт.", "success")

        
        
        next_page = request.args.get("next")
        if _is_safe_redirect(next_page):
            return redirect(next_page)
        return redirect(url_for("home.index"))

    return render_template("auth/login.html", form=form)
