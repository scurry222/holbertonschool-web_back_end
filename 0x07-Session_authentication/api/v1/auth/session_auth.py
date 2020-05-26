#!/usr/bin/env python3
""" Session authentication Module
"""
from api.v1.auth.auth import Auth
import uuid
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """ Class BasicAuth
        Provide authentication for a current session.

        Attributes:
            Auth(class): inherit auth class to gather headers and paths.

        Methods:
            create_session: Creates a session ID for a user_id.

            user_id_for_session_id: Return a User ID based on a Session ID.

            current_user: Return user instance based on the cookie value.

            destroy_session: Delete the user session or logout.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str=None) -> str:
        """ Use uuid to generate new key in dict, add user_id to key """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str=None) -> str:
        """ Retrieve link between User ID and a session ID """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get user associated with cookie and user ID """
        if not request:
            return None
        cookie = self.session_cookie(request)
        if not cookie:
            return None
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        if request is None:
            return None
        cookie = self.session_cookie(request)
        if not cookie:
            return False
        user_id = self.user_id_for_session_id(cookie)
        if not user_id:
            return False
        self.user_id_by_session_id.pop(cookie)
        return True
