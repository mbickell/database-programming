from utils import execute

def read_properties(cursor):
  execute("SELECT * FROM property")
  
  data = cursor.fetchall()
  return data

def print_properties(cursor):
  data = read_properties(cursor)

  for datum in data:
    print(f"id: {datum[0]}, code: {datum[1]}, name: {datum[2]}, location: {datum[3]}")

def get_property_by_code(cursor, property_code):
  execute(f"SELECT * FROM property WHERE code=\"{property_code}\"")

  data = cursor.fetchall()
  return data

def get_property_by_id(cursor, propertyID):
  execute(f"SELECT * FROM property WHERE id=\"{propertyID}\"")

  data = cursor.fetchone()
  return data