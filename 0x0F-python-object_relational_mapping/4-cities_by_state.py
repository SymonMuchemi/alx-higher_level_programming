#!/usr/bin/python3
"""runs a join query from state and cities tables"""
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
    cursor.execute("SELECT cities.id, cities.name, states.name \
        FROM cities \
        INNER JOIN states \
        ON cities.state_id = states.id \
        ORDER BY cities.id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
