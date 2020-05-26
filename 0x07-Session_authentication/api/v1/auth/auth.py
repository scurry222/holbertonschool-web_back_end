#!/usr/bin/env python3
""" Module of Authentication
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """ Class Auth
        Manage API authentication.

        Methods:
            require_auth: Continue authorizing if requested path is not in
                excluded paths.

            authorization_header: Validate all requests to secure the API.

            current_user: Do nothing, further implementation required.

            session_cookie: return a cookie value from a request.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Return requested path if not in the list of excluded paths. """
        if path is None or excluded_paths is None:
            return True
        if path[-1] is not "/":
            path += "/"

        wildcard_paths = [p[:-1] for p in excluded_paths if p.endswith('*')]

        for p in wildcard_paths:
            if path.startswith(p):
                return False

        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ Return the value of the header request 'Authorization'. """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Do nothing """
        return None

    def session_cookie(self, request=None):
        """ Return cookie value """
        if request is None:
            return None
        return request.cookies.get(getenv("SESSION_NAME"), None)
