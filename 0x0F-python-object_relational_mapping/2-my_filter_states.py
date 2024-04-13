#!/usr/bin/python3
"""FIlters states by user input"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    cursor.close()
    db.close()
