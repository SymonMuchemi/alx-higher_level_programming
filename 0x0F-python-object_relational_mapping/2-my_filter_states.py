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
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id".format(sys.argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
