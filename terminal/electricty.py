import crud.electricity.stats as stats

def get_property_code(filename):
  start_of_code_index = filename.index("/0") + 1
  end_of_code_index = filename.rindex('.')
  return filename[start_of_code_index:end_of_code_index]

def begin_stats_cli(cursor, mariadb):
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
          print(stats.get_total_entries(cursor, mariadb, propertyID))
        else:
          data = stats.get_group_by_total_entries(cursor, mariadb)
          for datum in data:
            print(f"ID: {datum[0]}, Name: {datum[1]}, Total: {datum[2]}")
      case "a":
        if propertyID:
          print(stats.get_average_value(cursor, mariadb, propertyID))
        else:
          data = stats.get_group_by_average_value(cursor, mariadb)
          for datum in data:
            print(f"ID: {datum[0]}, Name: {datum[1]}, Average: {datum[2]}")
      case "n":
        if propertyID:
          data = stats.get_minimum_value(cursor, mariadb, propertyID)
          print(f"value: {data[3]}, timestamp: {data[2]}")
        else:
          data = stats.get_group_by_minimum_value(cursor, mariadb)
          for datum in data:
            print(f"ID: {datum[0]}, Name: {datum[1]}, Minimum: {datum[2]}")
      case "m":
        if propertyID:
          data = stats.get_maximum_value(cursor, mariadb, propertyID)
          print(f"value: {data[3]}, timestamp: {data[2]}")
        else:
          data = stats.get_group_by_maximum_value(cursor, mariadb)
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