#!/usr/bin/env python3
"""
DB model
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """ DB class """

    def __init__(self):
        """ Initialize a new DB instance """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Memoized session object """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ save the user to the database """
        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        This method takes in arbitrary keyword arguments
        and returns the first row found in the users table
        as filtered by the method’s input arguments.
        """

        try:
            dec = list(kwargs.items())
            user = self._session.query(User).filter(
                getattr(User, dec[0][0]) == dec[0][1]).first()
        except InvalidRequestError:
            raise InvalidRequestError
        except AttributeError:
            raise NoResultFound
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """This method takes in arbitrary keyword arguments
        and returns the first row found in the users table
        as filtered by the method’s input arguments.
        """
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if not hasattr(user, k):
                raise ValueError
            else:
                setattr(user, k, v)
        self._session.commit()
