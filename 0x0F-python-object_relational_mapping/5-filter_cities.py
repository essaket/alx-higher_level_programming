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

    c.execute("SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            AND states.name = '{:s}'\
            ORDER BY cities.id ASC".format(sys.argv[4]))
    [l.append(x[0]) for x in c.fetchall()]
    print(", ".join(l))

    c.close()
    db.close()
