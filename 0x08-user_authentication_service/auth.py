#!/usr/bin/env python3
""" Auth module
"""

from user import User
from db import DB
from typing import TypeVar
import bcrypt
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Return a salted hash of the input password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

class Auth:
    """ Auth class
        Create and handle the authentication database.

        Methods:
            register_user: save a user to the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """ If user doesn't exist in db, add the, and return User object """
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError("User {email} already exists")
        new_user = self._db.add_user(email, _hash_password(password))
        return new_user