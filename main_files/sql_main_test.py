import sql_bridge
import core_functions

# host="localhost", user="root", passwd="2CTH6yan8RST", database="python_test"

my_conn, cur = sql_bridge.establish_connection(host="localhost", user="root",
                                               passwd="2CTH6yan8RST", database="python_test")
tables = sql_bridge.show_tables(my_conn, cur)
result = core_functions.table_tuple_separation(tables[2])
print(result)
