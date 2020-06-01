#!/usr/bin/env python3
""" User module
"""

from flask import Flask
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ Class User
        Creates a SQL alchemy model named User for a database table 'users'.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_password = Column(String(250))
    session_id = Column(String(250))
    reset_token = Column(String(250))
