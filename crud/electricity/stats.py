def stats_menu(cursor, mariadb):
  print("Select your property with it's id number OR enter [G] to group by property")

  user_input = input().lower()
  propertyID = None

  if user_input != "g":
    propertyID = int(user_input)

  while(1):
    print()
    
    if propertyID:
      print(f"Property with id {propertyID} selected, please select your operation")
    else:
      print("Grouping by properties")
    
    print("[T]otal, [A]verage, Mi[N], [M]ax, Change [P]roperty, [B]ack")
    command = input().lower()

    print()

    match command:
      case "t":
        if propertyID:
          print(get_total_entries(cursor, mariadb, propertyID))
        else:
          data = get_group_by_total_entries(cursor, mariadb)
          for datum in data:
            print(f"ID: {datum[0]}, Name: {datum[1]}, Total: {datum[2]}")
      case "a":
        if propertyID:
          print(get_average_value(cursor, mariadb, propertyID))
        else:
          data = get_group_by_average_value(cursor, mariadb)
          for datum in data:
            print(f"ID: {datum[0]}, Name: {datum[1]}, Average: {datum[2]}")
      case "n":
        if propertyID:
          data = get_minimum_value(cursor, mariadb, propertyID)
          print(f"value: {data[3]}, timestamp: {data[2]}")
        else:
          data = get_group_by_minimum_value(cursor, mariadb)
          for datum in data:
            print(f"ID: {datum[0]}, Name: {datum[1]}, Minimum: {datum[2]}")
      case "m":
        if propertyID:
          data = get_maximum_value(cursor, mariadb, propertyID)
          print(f"value: {data[3]}, timestamp: {data[2]}")
        else:
          data = get_group_by_maximum_value(cursor, mariadb)
          for datum in data:
            print(f"ID: {datum[0]}, Name: {datum[1]}, Maximum: {datum[2]}")
      case "p":
        print("Select a new property with it's id number")
        propertyID = int(input().lower())
      case "b":
        print("Going back...")
        break
      case _:
        print(command)


def get_total_entries(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT COUNT(*) FROM electricity WHERE property={propertyID}")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data[0]

def get_group_by_total_entries(cursor, mariadb):
  try:
    cursor.execute("""
                    SELECT property.id, property.name, COUNT(electricity.value) as total 
                    FROM electricity 
                    LEFT JOIN property
                    ON electricity.property = property.id
                    GROUP BY property
                  """)
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def get_average_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT AVG(value) FROM electricity WHERE property={propertyID}")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return round(data[0], 3)

def get_group_by_average_value(cursor, mariadb):
  try:
    cursor.execute("""
                    SELECT property.id, property.name, AVG(electricity.value) as total 
                    FROM electricity 
                    LEFT JOIN property
                    ON electricity.property = property.id
                    GROUP BY property
                  """)
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def get_minimum_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT * FROM electricity WHERE value = (SELECT min(value) FROM electricity WHERE property={propertyID})")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data

def get_group_by_minimum_value(cursor, mariadb):
  try:
    cursor.execute("""
                    SELECT property.id, property.name, MIN(electricity.value) as total 
                    FROM electricity 
                    LEFT JOIN property
                    ON electricity.property = property.id
                    GROUP BY property
                  """)
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def get_maximum_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT * FROM electricity WHERE value = (SELECT max(value) FROM electricity WHERE property={propertyID})")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data

def get_group_by_maximum_value(cursor, mariadb):
  try:
    cursor.execute("""
                    SELECT property.id, property.name, MAX(electricity.value) as total 
                    FROM electricity 
                    LEFT JOIN property
                    ON electricity.property = property.id
                    GROUP BY property
                  """)
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data