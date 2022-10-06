#!/usr/bin/env python3
""" 3. Auth class """

import re
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """
    Auth class that manage the API Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ class to manage the API authentication.
        """

        if path is None or excluded_paths == [] or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """ public method def authorization_header
        """

        if request is None:
            return None
        if request.headers.get('Authorization', None) is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method def current_user
        """

        return None

    def session_cookie(self, request=None):
        """the method def session_cookie"""
        if request is None:
            return None
        cookie_name = os.getenv("SESSION_NAME")
        return request.cookies.get(cookie_name)
