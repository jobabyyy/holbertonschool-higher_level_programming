#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Check if there are 4 arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        exit(1)

    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    # Create a cursor
    cur = db.cursor()

    # Create the SQL query using format with the user input
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cur.execute(query)

    # Print the results
    for row in cur.fetchall():
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
