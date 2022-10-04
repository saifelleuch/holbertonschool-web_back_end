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

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str)
        """ method def decode_base64_authorization_header """

        if decoded_base64_authorization_header is None:
            return(None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        emailAndPass = decoded_base64_authorization_header.split(':', 1)
        return tuple(emailAndPass)
