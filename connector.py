import os
from dotenv import load_dotenv

load_dotenv()

# connection parameters
connection_params = {
    "user" : os.getenv("MARIA_DB_USER"),
    "password" : os.getenv("MARIA_DB_PASSWORD"),
    "host" : os.getenv("MARIA_DB_HOST"),
    "database" : os.getenv("MARIA_DB_DB")
}


# retrieve data
def read_data(cursor, mariadb):
    try:
        cursor.execute("SELECT * FROM electricity")
    except mariadb.Error as e: 
        print(f"Error: {e}")

    data = cursor.fetchall()

    # print content
    for datum in data:
        print(f"id: {datum[0]}, property: {datum[1]} timestamp: {datum[2]}, value: {datum[3]}")

