import os
import mariadb
from dotenv import load_dotenv

load_dotenv()

# connection parameters
conn_params= {
    "user" : os.getenv("MARIA_DB_USER"),
    "password" : os.getenv("MARIA_DB_PASSWORD"),
    "host" : os.getenv("MARIA_DB_HOST"),
    "database" : "e2501254_test"
}

# Establish a connection
connection= mariadb.connect(**conn_params)

cursor= connection.cursor()

# Populate countries table  with some data


# retrieve data
cursor.execute("SELECT * FROM property")

# print content
row = cursor.fetchone()
print(*row, sep=' ')

# free resources
cursor.close()
connection.close()