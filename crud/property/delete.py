from utils import execute
from crud.property.read import get_property_by_code

def commit_property_deletion(cursor, connection, code):
  data = get_property_by_code(cursor, code)

  while (1):
    print(f"Property: code: {data[0]}, name: {data[1]}, location: {data[2]}")
    print("Is ready to be deleted, please press [Y] to commit or [N] to rollback")

    user_input = input().lower()

    match user_input:
      case "y":
        print("Committing...")
        delete_property(code)
        connection.commit()
        break
      case "n":
        print("Rolling back...")
        break
      case _:
        print("Command not recognised")

def request_code_to_delete():
  print("Enter the code of the property to be deleted e.g. 000-000-0000-0000")
  
  user_input = input().strip()

  return user_input

def delete_property(code):
  execute(f"DELETE FROM property WHERE code = \"{code}\"")

  
def get_property_by_code(cursor, code):
  execute(f"SELECT code, name, location FROM property WHERE code=\"{code}\"", limit=True)

  data = cursor.fetchone()
  return data