import sys
import mariadb
from connector import connection_params
from property import begin_cmd
from insert import insert_electricity

# Establish a connection
try:
    connection = mariadb.connect(**connection_params)

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = connection.cursor()

# insert_electricity(cursor, connection)
# read_data(cursor, mariadb)

begin_cmd(cursor, connection, mariadb)

# free resources
cursor.close()
connection.close()