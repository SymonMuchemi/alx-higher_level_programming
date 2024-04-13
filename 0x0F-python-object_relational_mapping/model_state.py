#!/usr/bin/python3
"""model class for the states object"""
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """Mapping of the state to the database"""
    __tablename__ = "states"

    # The columns in the table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
