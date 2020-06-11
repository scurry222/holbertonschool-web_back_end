#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel
import os

app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def home():
    """Home page"""

    return render_template("0-index.html")


# @app.route("/error")
# def error():
#     raise Exception("Error!")

if __name__ == "__main__":

    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
