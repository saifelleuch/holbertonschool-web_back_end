#!/usr/bin/env python3
""" 3. Auth class """

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Auth class that manage the API Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ class to manage the API authentication.
        """

        return False
    
    def authorization_header(self, request=None) -> str:
        """ public method def authorization_header
        """

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method def current_user
        """

        return None
