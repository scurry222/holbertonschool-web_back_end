#!/usr/bin/env python3

""" View for session auth module
"""
from flask import jsonify, request, abort
from models.user import User
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Send credentials and verify """
    user_email = request.form.get('email')
    if not user_email:
        return jsonify({"error": "email missing"}), 400

    user_pwd = request.form.get('password')
    if not user_pwd:
        return jsonify({"error": "password missing"}), 400

    try:
        search = User.search({"email": user_email})
    except BaseException:
        return jsonify({"error": "no user found for this email"}), 404

    if not search:
        return jsonify({"error": "no user found for this email"}), 404

    for user in search:
        if not user.is_valid_password(user_pwd):
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        response = jsonify(user.to_json())
        response.set_cookie(getenv('SESSION_NAME'), session_id)
        return response
    return jsonify({"error": "no user found for this email"}), 404


@app_views.route('/auth_session/logout', methods=['DELETE'],\
     strict_slashes=False)
def delete():
    """ remove a session """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
