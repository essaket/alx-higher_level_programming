#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()

    c.execute("SELECT cities.id, cities.name, states.name FROM\
            cities INNER JOIN states ON states.id=cities.state_id")
    [print(x) for x in c.fetchall()]

    c.close()
    db.close()
