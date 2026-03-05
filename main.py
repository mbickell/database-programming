import sys
import mariadb
from connector import connection_params, read_data, insert_electricity

# Establish a connection
try:
    connection = mariadb.connect(**connection_params)

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = connection.cursor()

# insert_electricity(cursor)
# read_data(cursor, mariadb)

# free resources
cursor.close()
connection.close()