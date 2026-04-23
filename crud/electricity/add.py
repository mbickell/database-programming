import json
from utils import execute


def read_json_data(filename):
    try:
        with open(filename, encoding="utf8") as json_file:
            return json.load(json_file)
    except:
        print("File not opened")

# Populate countries table  with some data


def insert_electricity(connection, json_data, property_id):
    for datum in json_data:
        execute(
            "INSERT INTO electricity (property,timestamp,value) VALUES (?, ?, ?)",
            (property_id, datum['timestamp'], datum['value']))
    connection.commit()
