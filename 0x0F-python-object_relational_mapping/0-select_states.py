#!/usr/bin/python3
"""list all states from the hbtn_0e_0_usa database"""
import sys
import MySQLdb

# connecting to the database
connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )

cursor = connection.cursor()

cursor.execute("SELECT * FROM states ORDER BY id")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
