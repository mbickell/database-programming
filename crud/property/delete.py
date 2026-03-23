from utils import execute
from crud.property.read import get_property_by_id

def commit_property_deletion(cursor, connection, id):
  data = get_property_by_id(cursor, id)

  while (1):
    print(f"Property: {data}")
    print("Is ready to be deleted, please press [Y] to commit or [N] to rollback")

    user_input = input().lower()

    match user_input:
      case "y":
        print("Committing...")
        delete_property(id)
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

def delete_property(id):
  execute(f"DELETE FROM property WHERE id = {id}")