#!/usr/bin/python3
"""
 Displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    mysql_user, mysql_pass, db_name, search_str = args
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_user,
        password=mysql_pass,
        port=3306,
        database=db_name,
    )
    QUERY = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(
        search_str)

    db.query(QUERY)

    rows = db.store_result().fetch_row(maxrows=0)
    for row in rows:
        print(row)
