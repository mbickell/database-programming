import csv
from datetime import datetime
from decimal import Decimal
from connector import cursor, connection

with open("./data/electricity_prices.csv", mode='r', newline='') as file:
    csvFile = csv.DictReader(file)
    data = []
    for lines in csvFile:
        # print(lines)
        if lines["price"]:
            data.append((
                lines["country"],
                lines["iso3_code"],
                # fix to "proper" date
                datetime.strptime(lines["date"], "%Y-%m-%d").date(),
                Decimal(lines["price"])  # fix to "proper" decimal
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
