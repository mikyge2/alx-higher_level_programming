#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
"""
if __name__ == '__main__':
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in data:
        print('{}: {} -> {}'.format(city.id, city.name, state.name))
    session.close()
