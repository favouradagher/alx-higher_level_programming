#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )

    # Create a cursor object
    cur = db.cursor()

    # Use a parameterized query to prevent SQL injection
    query = """
            SELECT GROUP_CONCAT(name SEPARATOR ', ')
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    
    # Execute the query with user input as a parameter
    cur.execute(query, (state_name,))

    # Fetch the result
    result = cur.fetchone()

    # Display the results
    if result[0] is not None:
        print(result[0])

    # Close cursor and connection
    cur.close()
    db.close()

