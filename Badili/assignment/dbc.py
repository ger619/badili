import mysql.connector


def dbconnect(dbName, dbUser, dbPass, dbPort = 3306, dbHost = 'localhost'):
    #create connection
    return mysql.connector.connect(database = dbName , user = dbUser, host = dbHost, password = dbPass, port = dbPort)
