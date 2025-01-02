#!/usr/bin/env python3
"""
Session Authentication module
"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    Sessiom Auth, a new authentication mechanism
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        overload that returns a User instance based on a cookie value
        """
        if request:
            _my_session_id = self.session_cookie(request)
            if _my_session_id:
                user_id = self.user_id_for_session_id(_my_session_id)
                return User.get(user_id)

    def destroy_session(self, request=None):
        """
        method that deletes the user session / logout
        """
        if request is None:
            return False
        _my_session_id = self.session_cookie(request)
        if not _my_session_id:
            return False
        user_id = self.user_id_for_session_id(_my_session_id)
        if not user_id:
            return False
        del self.user_id_by_session_id[_my_session_id]
        return True