import json

# Populate countries table  with some data
def insert_electricity(cursor, connection):
    json_data = read_json_data()
    for datum in json_data:
        cursor.execute(
            "INSERT INTO electricity (property,timestamp,value) VALUES (?, ?, ?)", 
            (1, datum['timestamp'], datum['value']))
    connection.commit()

def read_json_data():
  try:
    with open('./data/electricity.json') as json_file:
      return json.load(json_file)
  except:
    print("File not opened")

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

