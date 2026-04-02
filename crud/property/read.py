from utils import execute

def read_properties(cursor):
  execute("SELECT code, name, location FROM property")
  
  data = cursor.fetchall()
  return data

def print_properties(cursor):
  data = read_properties(cursor)

  for datum in data:
    print(f"code: {datum[0]}, name: {datum[1]}, location: {datum[2]}")

def get_property_by_code(cursor, property_code):
  execute(f"SELECT id, code, name, location FROM property WHERE code=\"{property_code}\"")

  data = cursor.fetchall()
  return data
