#!/usr/bin/env python3
"""
    Database Authentication Module
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import timedelta, datetime, timezone


class SessionDBAuth(SessionExpAuth):
    """ Class SessionDBAuth

        Save session ID if application stops.

        Methods:
            create_session: creates and stores new instance of UserSession and
                            returns the Session ID.

            user_id_for_session_id: returns the User ID by requesting
                                    UserSession in the database based on
                                    session_id.

            destroy_session: Remove a UserSession based on the session ID from
                             the reequest cookie.
    """
    def create_session(self, user_id=None):
        """ Save an instance of the user session """
        if user_id is None:
            return None

        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return the user ID at the current session ID """
        if session_id is None:
            return None
        try:
            sessions = UserSession.search({session_id: session_id})
            if sessions is None:
                return None

            session_time = timedelta(seconds=self.session_duration)

            if sessions[0].created_at + session_time < datetime.utcnow():
                return None

            return sessions[0].user_id
        except ValueError:
            return None

    def destroy_session(self, request=None):
        """ Destroy a current session """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        try:
            sessions = UserSession.search({session_id: session_id})
            if sessions is None:
                return False

            sessions[0].remove()

            return True

        except ValueError:
            return False
