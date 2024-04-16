#!/usr/bin/python3
"""Lists all States with a letter 'a'"""
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

    for state in session.query(State).order_by(State.id).all():
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")

    session.close()
