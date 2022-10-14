#!/usr/bin/env python3
"""
4. Hash password
"""

import bcrypt


def _hash_password(password: str) -> str:
    """
    takes in a password string
    arguments and returns bytes
    """

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
