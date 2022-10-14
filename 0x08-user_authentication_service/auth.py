#!/usr/bin/env python3
"""
4. Hash password
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    takes in a password string
    arguments and returns bytes
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

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
