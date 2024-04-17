#!/usr/bin/python3
"""Adds Louisiana to state database adn prints state id"""
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
    found = False

    louisiana = State(name='Louisiana')

    session.add(louisiana)

    for state in session.query(State):
        if state.name == 'Louisiana':
            print("{}".format(state.id))
            found = True

    if found is False:
        print("Not found")

    session.close()
