#!/usr/bin/python3
"""
Module States
script that lists all cities from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    MY_USER = argv[1]
    MY_PASSWD = argv[2]
    MY_DB = argv[3]

    '''Open Database connection'''
    mydb = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=MY_USER,
                           passwd=MY_PASSWD,
                           db=MY_DB)

    '''Create cursor for operate over DB'''
    myCursor = mydb.cursor()

    '''Write an sql query to get list of cities'''
    sql = "select * from cities order by cities.id asc"

    '''pass and execute a SQL sentence'''
    myCursor.execute(sql)

    '''retrive records and fill cursor'''
    cities = myCursor.fetchall()

    '''Print rows'''
    for city in cities:
        print(city)

    '''close cursor'''
    myCursor.close()

    '''close connection to DB'''
    mydb.close()
