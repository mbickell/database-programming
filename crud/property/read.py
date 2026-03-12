def read_properties(cursor, mariadb):
  try:
    cursor.execute("SELECT * FROM property")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def print_properties(cursor, mariadb):
  data = read_properties(cursor, mariadb)

  for datum in data:
    print(f"id: {datum[0]}, code: {datum[1]}, name: {datum[2]}, location: {datum[3]}")

def get_property(cursor, mariadb, property_code):
  try:
    cursor.execute(f"SELECT * FROM property WHERE code=\"{property_code}\"")
  except mariadb.Error as e:
    print(f"Error: {e}")

  data = cursor.fetchall()
  return data