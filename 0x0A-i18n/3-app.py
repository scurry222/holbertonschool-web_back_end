#!/usr/bin/env python3
""" Flask app module
"""

from flask import Flask, render_template, request, flash
from flask_babel import Babel, _
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
def get_locale():
    """ Return best match from accepted languages """
    if request.args.get("locale") in Config.LANGUAGES:
        return request.args.get("locale")
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """ Home page """
    flash(_('[home_title] Welcome to Holberton'))
    flash(_('[home_header] Hello World!'))
    return render_template("3-index.html")


# @app.route("/error")
# def error():
#     raise Exception("Error!")

if __name__ == "__main__":

    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(debug=DEBUG, host="127.0.0.1", port=PORT)
