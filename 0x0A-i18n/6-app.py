#!/usr/bin/env python3
""" Flask app module
"""

from flask import Flask, render_template, request, flash, g
from flask_babel import Babel, _
from typing import Optional, Union
import gettext
import os

app = Flask(__name__)
babel = Babel(app)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")

# Creating a user login system is outside the scope of this project.
# This dictionary is to simulate a similar behavior:
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Configuration of available languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user(login_as: int) -> Union[dict, None]:
    """ Get dictionary based on user_id """
    try:
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """ Set user before other functions run """
    if request.args.get("login_as"):
        user = get_user(request.args.get("login_as"))
        if user:
            g.user = user["name"]
        else:
            return None
    else:
        return None


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Return best match from accepted languages """
    if request.args.get("locale"):
        return request.args.get("locale")

    if request.args.get("login_as"):
        user = get_user(request.args.get("login_as"))
        if user and user["locale"] in app.config['LANGUAGES']:
            user.get("locale")

    if request.headers.get("locale"):
        return request.headers.get("locale")

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ Home page """
    return render_template("6-index.html")


# @app.route("/error")
# def error():
#     raise Exception("Error!")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
