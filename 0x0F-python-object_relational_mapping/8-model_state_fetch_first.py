#!/usr/bin/python3
"""Lists all State objects from the database"""
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

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()
