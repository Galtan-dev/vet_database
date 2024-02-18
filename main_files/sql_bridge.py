"""
script with mysql functions
"""
import mysql.connector

# host="localhost", user="root", passwd="2CTH6yan8RST", database="python_test"


def establish_connection(host, user, passwd, database):
    """
    function for establishing connection with mysql database
    """
    # create connection
    my_conn = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
    # creating the cursor object
    cur = my_conn.cursor()

    return my_conn, cur


def create_table(table_name, my_conn, cur):
    """
    function for creating new table with define name and with primary key
    """
    try:
        # command for creating table, try block for possibility there is a table with same name
        cur.execute(f"create table {table_name}(ID_num int(20) not null primary key)")
    except:
        my_conn.rollback()


def disconnection(my_conn):
    """
    function for disconnecting from server
    """
    my_conn.close()


def show_columns(table_name, my_conn, cur):
    """
    function for visualization of columns of table
    """
    columns = []
    try:
        # command for showing of columns of table
        cur.execute(f"show columns {table_name}")
    except:
        my_conn.rollback()

    # check what is saved in cur variable and iterates through it
    for x in cur:
        columns.append(x)

    return columns


def show_tables(my_conn, cur):
    """
    function for visualization of tables of database
    """
    tables = []
    try:
        # command for showing of tables of database
        cur.execute("show tables")
    except:
        my_conn.rollback()

    # check what is saved in cur variable and iterates through it
    for x in cur:
        tables.append(x)

    return tables
