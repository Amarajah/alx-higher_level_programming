#!/usr/bin/python3

'''
script that adds new State object
to the database hbtn_0e_6_usa
'''


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Create a new State object and add it to the session'''
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    '''Print the id of the new State object'''
    print('{}'.format(new_state.id))
