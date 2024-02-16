import mysql.connector

myconection = mysql.connector.connect(host="localhost", user="root", passwd="2CTH6yan8RST")

cur = myconection.cursor()

try:
    cur.execute("create database Python_test")
    dbs = cur.execute("show databases")
except:
    myconection.rollback()
for x in cur:
    print(x)
myconection.close()