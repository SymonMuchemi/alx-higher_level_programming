#!/usr/bin/python3
"""Lists all State objects from the database"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

nm = sys.argv[1]
pw = sys.argv[2]
dn = sys.argv[3]
engine = create_engine(
        f'mysql+mysqldb://{nm}:{pw}@localhost/{dn}',
        pool_pre_ping=True
)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

session.close()
