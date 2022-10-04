#!/usr/bin/env python3
"""
a class BasicAuth that inherits from Auth
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ BasicAuthentication class that inherits from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ method def extract_base64_authorization_header """

        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ method def decode_base64_authorization_header """

        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        if self.isBase64(base64_authorization_header) is False:
            return None
        return base64.b64decode(base64_authorization_header).decode('utf-8')
