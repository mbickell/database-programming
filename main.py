import mariadb
from connector import cursor, connection
from terminal.property import begin_cmd

begin_cmd(cursor, connection, mariadb)

# free resources
cursor.close()
connection.close()