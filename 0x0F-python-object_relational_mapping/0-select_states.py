#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Execute the query to select all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

