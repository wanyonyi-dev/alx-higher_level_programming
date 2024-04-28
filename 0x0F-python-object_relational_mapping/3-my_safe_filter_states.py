#!/usr/bin/python3

import MySQLdb
from sys import argv


def state():
    """takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument"""

    try:
        db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3])
    except Exception:
        print("unable to connect to the database")
        return 0
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for i in rows:
        for b in i:
            if type(b) == str and b == argv[4]:
                print(i)
    cur.close()
    db.close()


state()
