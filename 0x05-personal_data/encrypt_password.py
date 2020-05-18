#!/usr/bin/env python3
"""
    Password encryption module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ hash and salt input password  """
    if password:
        bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check validity of password """
    if hashed_password and password:
        return bcrypt.checkpw(password, hashed_password)
