#!/usr/bin/python3
"""runs a join query from state and cities tables and filter by state"""
import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )

    cursor = connection.cursor()
    query = "SELECT * FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id"

    name = (sys.argv[4],)
    cursor.execute(query, name)

    rows = cursor.fetchall()

    print(", ".join([ct[2] for ct in rows if ct[4] == sys.argv[4]]))
