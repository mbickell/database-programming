import json

def read_json_data(filename):
  try:
    with open(filename) as json_file:
      return json.load(json_file)
  except:
    print("File not opened")

# Populate countries table  with some data
def insert_electricity(cursor, connection, json_data, property_id):
    for datum in json_data:
        cursor.execute(
            "INSERT INTO electricity (property,timestamp,value) VALUES (?, ?, ?)", 
            (property_id, datum['timestamp'], datum['value']))
    connection.commit()