from flask import Blueprint, render_template

bp = Blueprint(name="pages", import_name=__name__)


@bp.route("/")
def home():
    return render_template("pages/home.html")


@bp.route("/menu")
def menu():
    return render_template("pages/menu.html")
