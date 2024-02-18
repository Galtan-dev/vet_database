import mysql.connector

# create connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="2CTH6yan8RST", database="python_test")

# creating the cursor object
cur = myconn.cursor()

try:
    cur.execute("create table Getr("
                      "name varchar(20) not null, "
                      "id int(20) not null primary key, "
                      "salary float not null, "
                      "Dept_id int not null)")

except:
    myconn.rollback()

myconn.close()