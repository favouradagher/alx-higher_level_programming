#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create a session
    with Session(engine) as session:
        # Add a new State object with the name "Louisiana"
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        # Print the new states.id after creation
        print(new_state.id)

