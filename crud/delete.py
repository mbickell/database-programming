def commit_property_deletion(cursor, mariadb, connection, id):
  data = select_property_with_id(cursor, mariadb, id)

  while (1):
    print(f"Property: {data}")
    print("Is ready to be deleted, please press [Y] to commit or [N] to rollback")

    user_input = input().lower()

    match user_input:
      case "y":
        print("Committing...")
        delete_property(cursor, mariadb, id)
        connection.commit()
        break
      case "n":
        print("Rolling back...")
        break
      case _:
        print("Command not recognised")

def request_id_to_delete():
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

def delete_property(cursor, mariadb, id):
  try:
    cursor.execute(f"DELETE FROM property WHERE id = {id}")
  except mariadb.Error as e:
    print(f"Error: {e}")