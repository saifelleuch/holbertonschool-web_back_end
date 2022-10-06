#!/usr/bin/env python3
"""
0x07-Session_authentication
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """class SessionAuth that inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ instance method def create_session """
        if user_id is None:
            return None

        if type(user_id) is not str:
            return None
        self.id = str(uuid.uuid4())
        self.__class__.user_id_by_session_id[self.id] = user_id
        return self.id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ instance method def user_id_for_session_id """
        if session_id is None or type(session_id) is not str:
            return None
        sessions = self.__class__.user_id_by_session_id
        userId = sessions.get(session_id, None)
        return userId
