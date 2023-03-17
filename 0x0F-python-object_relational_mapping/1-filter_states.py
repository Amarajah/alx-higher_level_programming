#!/usr/bin/python3
"""
Module States
script that lists all states with capital N
from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    MY_USER = argv[1]
    MY_PASSWD = argv[2]
    MY_DB = argv[3]

    '''Open Database connection'''
    mydb = MySQLdb.connect(host="localhost",
                           user=MY_USER,
                           passwd=MY_PASSWD,
                           db=MY_DB,
                           port=3306)

    '''Create cursor for operate over DB'''
    myCursor = mydb.cursor()

    '''pass and execute a SQL sentence'''
    myCursor.execute("select * from states \
                     WHERE name LIKE 'N%'\
                     ORDER BY id ASC")

    '''retrive records and fill cursor'''
    states = myCursor.fetchall()

    '''Print rows'''
    for state in states:
        print(state)

    '''close cursor'''
    myCursor.close()

    '''close connection to DB'''
    mydb.close()
