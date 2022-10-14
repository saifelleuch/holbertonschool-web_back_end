#!/usr/bin/env python3
"""
4. Hash password
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """
    takes in a password string
    arguments and returns bytes
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """generate uuid
    """

    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """instantiate
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registre new user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(user))
        except NoResultFound:
            pass
        hashed = _hash_password(password)
        return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """It should expect email and password
        required arguments and return a boolean.
        """

        if email is None or password is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            encodedPassword = password.encode('utf-8')
            if user:
                if bcrypt.checkpw(encodedPassword, user.hashed_password):
                    return True
                else:
                    return False
            else:
                False
        except Exception as e:
            return False

    def create_session(self, email: str) -> str:
        """The method should find the user corresponding to the email,
        generate a new UUID and store it in the
        database as the user’s session_id, then return the session ID.
        """

        if email is None:
            return None
        try:
            user = self._db.find_user_by(email=email)
            if user:
                sid = _generate_uuid()
                self._db.update_user(user.id, session_id=sid)
                return sid
            else:
                return None

        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """It takes a single session_id string argument
        and returns the corresponding User or None
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception as e:
            return None

    def destroy_session(self, user_id: int) -> None:
        """takes a single user_id integer argument and returns None.
        The method updates the corresponding user’s session ID to None.
        """
        if not user_id:
            return None
        try:
            user = self._db.update_user(user_id, session_id=None)
            return None
        except Exception as e:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ It take an email string
        argument and returns a string.
        """

        if not email:
            raise ValueError
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            self._db.update_user(user.id, reset_token=uuid)
        except Exception as e:
            raise ValueError
        return uuid

    def update_password(self, reset_token, password):
        """It takes reset_token string argument
        and a password string argument and returns None.
        """
        if reset_token is None or password is None:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed)
            self._db.update_user(user.id, reset_token=None)

        except Exception as e:
            raise ValueError
        return None
