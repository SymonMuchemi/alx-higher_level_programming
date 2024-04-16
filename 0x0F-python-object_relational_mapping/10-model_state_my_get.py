#!/usr/bin/python3
"""prints the state with the name passed as an argument"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    nm = sys.argv[1]
    pw = sys.argv[2]
    dn = sys.argv[3]
    name = sys.argv[4]
    engine = create_engine(
            f'mysql+mysqldb://{nm}:{pw}@localhost/{dn}',
            pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    found = False

    for state in session.query(State):
        if state.name == name:
            print("{}".format(state.id))
            found = True

    if found is False:
        print("Not found")

    session.close()
