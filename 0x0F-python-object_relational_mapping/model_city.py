#!/usr/bin/python3
"""model class for the cities object"""
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class City(Base):
    """Mapping of the city to the database"""
    __tablename__ = "cities"

    # The columns in the table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
