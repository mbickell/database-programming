from terminal.electricty import begin_stats_cli
from crud.property.read import print_properties
from crud.property.add import request_property, add_property, commit_property_add
from crud.property.delete import request_id_to_delete, commit_property_deletion

def begin_property_cli(cursor, connection, mariadb):
  while(1):
    print("Select your operation ([L]ist, [A]dd, [D]elete, E[X]it, [S]tats)")
    command = input().lower()

    print()

    match command:
      case "l":
        print_properties(cursor)
      case "a":
        property = request_property()
        add_property(property)
        commit_property_add(connection, property)
      case "d":
        id = request_id_to_delete()
        commit_property_deletion(cursor, mariadb, connection, id)
      case "s":
        begin_stats_cli(cursor, mariadb)
      case "x":
        print("Exiting...")
        break
      case _:
        print(command)

    print()
