#!/usr/bin/env python3
""" Flask app module
"""

from flask import Flask, render_template, request, flash
from flask_babel import Babel, _
from typing import Optional
import gettext
import os

app = Flask(__name__)
babel = Babel(app)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "ABCDEF")


class Config:
    """ Configuration of available languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Return best match from accepted languages """
    if request.args.get("locale") in Config.LANGUAGES:
        return request.args.get("locale")
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ Home page """
    flash(_('[home_title] Welcome to Holberton'))
    flash(_('[home_header] Hello World!'))
    return render_template("4-index.html")


# @app.route("/error")
# def error():
#     raise Exception("Error!")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
