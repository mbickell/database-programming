from stats import stats_menu

def begin_cmd(cursor, connection, mariadb):
  while(1):
    print("Select your operation ([L]ist, [A]dd, [D]elete, E[X]it, [S]tats)")
    command = input().lower()

    print()

    match command:
      case "l":
        print_properties(cursor, mariadb)
      case "a":
        property = request_property()
        add_property(cursor, property)
        commit_property_add(connection, property)
      case "d":
        id = delete_property()
        commit_property_deletion(cursor, mariadb, connection, id)
      case "s":
        stats_menu(cursor, mariadb, connection)
      case "x":
        print("Exiting...")
        break
      case _:
        print(command)

    print()

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

def add_property(cursor, property):
  cursor.execute(
    "INSERT INTO property (code,name,location) VALUES (?, ?, ?)",
    (property["code"], property["name"], property["location"])
  )

def request_property():
  print("Give details of a property to add in semi-colon (;) seperated list in the format: code; name; location")
  print("e.g: 091-010-0669-0001; 2418 Päiväkoti Ariel; 2418 Päiväkoti Ariel")

  user_input = input().split(';')

  property = {
    "code": user_input[0].strip(),
    "name": user_input[1].strip(),
    "location": user_input[2].strip()
  }

  return property

def commit_property_add(connection, property):
  
  while (1):
    print(f"Property with values - code: {property["code"]}, name: {property["name"]}, location: {property["location"]}")
    print("Is ready to commit, please press [Y] to commit or [N] to rollback")

    user_input = input().lower()

    match user_input:
      case "y":
        print("Committing...")
        connection.commit()
        break
      case "n":
        print("Rolling back...")
        connection.rollback()
        break
      case _:
        print("Command not recognised")

def commit_property_deletion(cursor, mariadb, connection, id):
  data = select_property_with_id(cursor, mariadb, id)

  while (1):
    print(f"Property: {data}")
    print("Is ready to be deleted, please press [Y] to commit or [N] to rollback")

    user_input = input().lower()

    match user_input:
      case "y":
        print("Committing...")
        cursor.execute(f"DELETE FROM property WHERE id = {id}")
        connection.commit()
        break
      case "n":
        print("Rolling back...")
        break
      case _:
        print("Command not recognised")

def delete_property():
  print("Enter the id of the property to be deleted")
  
  user_input = input().strip()

  return user_input

def select_property_with_id(cursor, mariadb, id):
  try:
    cursor.execute(f"SELECT * FROM property WHERE id = {id}")
  except mariadb.Error as e:
    print(f"Error: {e}")

  data = cursor.fetchone()

  return data