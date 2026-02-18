import os
import mariadb
import sys
import json
from dotenv import load_dotenv

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

# Populate countries table  with some data

json_data = json.load(open('./data/electricity.json'))
for datum in json_data:
    cursor.execute(
        "INSERT INTO electricity (property,timestamp,value) VALUES (?, ?, ?)", 
        (1, datum['timestamp'], datum['value']))

# connection.commit()

# retrieve data
try:
    cursor.execute("SELECT * FROM electricity")
except mariadb.Error as e: 
    print(f"Error: {e}")

data = cursor.fetchall()

# print content
for datum in data:
    print(f"id: {datum[0]}, property: {datum[1]} timestamp: {datum[2]}, value: {datum[3]}")

# free resources
cursor.close()
connection.close()