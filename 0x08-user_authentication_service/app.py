#!/usr/bin/env python3
""" Flask app entry point
"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect
from db import DB


AUTH = Auth()
app = Flask(__name__)


@app_views.route('/', methods=['GET'], strict_slashes=False)
def french_welcome() -> str:
    """ Welcome page """
    return jsonify({"message":"Bienvenue"}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Authenticate user """
    email = request.form.get('email')
    password = request.form('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email}, {"message", "user created"}), 200
    except Exception:
        return jsonify({"message", "email already registered"}), 400


@app_views.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ Login function to respond to the /sessions route """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app_views.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Empty session id and redirect """
    s_id = request.cookies.get("session_id")
    user = DB.find_user_by(s_id)
    if user:
        AUTH.destroy_session(user)
        return redirect(url_for(french_welcome))
    else:
        abort(403)


@app_views.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ Find profile in db """
    s_id = request.cookies.get('session_id')
    user = DB.find_user_by(s_id)
    if user:
        return jsonify({"email", user.email}), 200
    else:
        abort(403)


@app_views.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
