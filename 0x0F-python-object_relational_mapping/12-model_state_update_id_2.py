#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
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
        # Get the State with id = 2
        state_to_update = session.query(State).filter_by(id=2).first()

        # Update the name to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()

