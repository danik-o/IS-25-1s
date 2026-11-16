

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user

from app.extensions import db
from app.models.user import User
from app.forms.register_form import RegisterForm

bp = Blueprint("register", __name__)


@bp.route("/register", methods=["GET", "POST"])
def register_page():
    
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))

    form = RegisterForm()

    
    
    print(form.data)
    if form.validate_on_submit():
        user = User(
            username=form.username.data.strip(),
            email=form.email.data.strip().lower(),
        )
        user.set_password(form.password.data)

        db.session.add(user)      
        db.session.commit()       

        flash("Регистрация прошла успешно! Теперь войдите.", "success")
        return redirect(url_for("login.login_page"))

    
    return render_template("auth/register.html", form=form)
