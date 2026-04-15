import csv
import os
import sys
from dotenv import load_dotenv
import mariadb
from datetime import datetime
from decimal import Decimal

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

with open("./data/electricity_prices.csv", mode='r', newline='') as file:
  csvFile = csv.DictReader(file)
  data = []
  for lines in csvFile:
    # print(lines)
    if lines["price"]:
       data.append((
          lines["country"],
          lines["iso3_code"],
          datetime.strptime(lines["date"], "%Y-%m-%d").date(), # fix to "proper" date
          Decimal(lines["price"]) # fix to "proper" decimal
       ))

# user on duplicate key update to manage double entries
query = """
      INSERT INTO prices (country, iso3_code, date, price_eur_mwhe) 
      VALUES (?, ?, ?, ?) 
      ON DUPLICATE KEY UPDATE 
      country = VALUES(country), 
      price_eur_mwhe = VALUES(price_eur_mwhe)
      """

# print(data)

cursor.executemany(query, data)

connection.commit()