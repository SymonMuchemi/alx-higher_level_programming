#!/usr/bin/python3
"""Deletes all states in the state table"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
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

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)

    session.commit()

    session.close()
