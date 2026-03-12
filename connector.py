import os
import sys
from dotenv import load_dotenv
import mariadb

load_dotenv()

# connection parameters
connection_params = {
    "user" : os.getenv("MARIA_DB_USER"),
    "password" : os.getenv("MARIA_DB_PASSWORD"),
    "host" : os.getenv("MARIA_DB_HOST"),
    "database" : os.getenv("MARIA_DB_DB")
}

# Establish a connection
try:
    connection = mariadb.connect(**connection_params)

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = connection.cursor()