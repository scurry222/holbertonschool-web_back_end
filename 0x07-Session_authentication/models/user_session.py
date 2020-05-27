#!/usr/bin/env python3
"""
    User Session Module
"""
from models.base import Base


class UserSession(Base):
    """ Class User Session

        Instantiate user_id and session_id.
    """
    def __init__(self, *args: list, **kwargs: dict):
        """ Construct user_id and session_id """
        super().__init__(*args, **kwargs)

        if kwargs.get('user_id') is not None:
            self.user_id = kwargs.get('user_id')

        if kwargs.get('session_id') is not None:
            self.session_id = kwargs.get('session_id')
