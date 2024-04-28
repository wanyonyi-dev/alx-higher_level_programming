#!/usr/bin/python3

import MySQLdb
from sys import argv


def state_id():
    """t lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa"""
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
        )
    except Exception:
        print("unable to connect to the database")
        return 0
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for state in rows:
        if isinstance(state[1], str) and state[1].startswith("N"):
            print(state)
    cur.close()
    db.close()


state_id()
