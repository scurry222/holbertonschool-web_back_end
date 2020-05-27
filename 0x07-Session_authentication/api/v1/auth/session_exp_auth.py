#!/usr/bin/env python3
"""
    Authentication experation module
"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Class Session Expiration Authentication

        Add Expiration time to session.

        Methods:
            create_session: Add date created to current session.

            user_id_for_session_id: Remove session if time exceeds
                                    variable time.
    """
    def __init__(self):
        """ Constructor for session duration """
        duration = getenv("SESSION_DURATION")

        if duration:
            self.session_duration = int(duration)
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Add dictionary with time created to dictionary of
         the current session """
        if user_id is None:
            return None

        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        user_id = self.user_id_by_session_id.get(session_id)
        if user_id is None:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return user_id from session dictionary if time alotted
            doesnt exceed specific time """
        if session_id is None:
            return None

        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None

        user_id = session_dictionary.get('user_id')
        if user_id is None:
            return None

        if self.session_duration <= 0:
            return user_id

        created_time = session_dictionary.get('created_at')
        if created_time is None:
            return None

        if datetime.now() > created_time + \
                timedelta(seconds=self.session_duration):
            return None

        return user_id
