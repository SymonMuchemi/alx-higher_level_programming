#!/usr/bin/python3
"""Lists all State objects from the database"""
from model_state import Base, State
from model_city import City
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

    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
