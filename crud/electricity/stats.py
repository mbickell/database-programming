def stats_menu(cursor, mariadb, connection):
  print("Select your property with it's id number")
  propertyID = int(input().lower())

  while(1):
    print()
    
    print(f"Property with id {propertyID} selected, please select your operation")
    print("[T]otal, [A]verage, Mi[N], [M]ax, Change [P]roperty, [B]ack")
    command = input().lower()

    print()

    match command:
      case "t":
        print(get_total_entries(cursor, mariadb, propertyID))
      case "a":
        print(get_average_value(cursor, mariadb, propertyID))
      case "n":
        data = get_minimum_value(cursor, mariadb, propertyID)
        print(f"value: {data[3]}, timestamp: {data[2]}")
      case "m":
        data = get_maximum_value(cursor, mariadb, propertyID)
        print(f"value: {data[3]}, timestamp: {data[2]}")
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
    cursor.execute(f"SELECT count(*) FROM electricity WHERE property={propertyID}")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data[0]

def get_average_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT avg(value) FROM electricity WHERE property={propertyID}")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return round(data[0], 3)

def get_minimum_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT * FROM electricity WHERE value = (SELECT min(value) FROM electricity WHERE property={propertyID})")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data

def get_maximum_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT * FROM electricity WHERE value = (SELECT max(value) FROM electricity WHERE property={propertyID})")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data