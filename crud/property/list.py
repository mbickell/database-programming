def list_propeties(cursor, mariadb):
  try:
    cursor.execute("SELECT * FROM property")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def print_properties(cursor, mariadb):
  data = list_propeties(cursor, mariadb)

  for datum in data:
    print(f"id: {datum[0]}, code: {datum[1]}, name: {datum[2]}, location: {datum[3]}")