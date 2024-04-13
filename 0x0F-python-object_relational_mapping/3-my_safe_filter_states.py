#!/usr/bin/python3
"""FIlters states by user input"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )
    cursor = db.cursor()
    query = "SELECT * FROM states \
            WHERE BINARY name = %s \
            ORDER BY id"
    name = (sys.argv[4],)
    cursor.execute(query, name)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
