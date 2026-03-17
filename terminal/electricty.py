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
    
    print("[T]otal, [A]verage, Mi[N], [M]ax, Change [P]roperty, Switch to [G]roup by mode, [B]ack")
    command = input().lower()

    print()

    match command:
      case "p":
        print("Select a new property with it's id number")
        propertyID = int(input().lower())
      case "g":
        propertyID = None
      case "b":
        print("Going back...")
        break
      case _:
        if propertyID:
          property_handler(cursor, mariadb, propertyID, command)
        else:
          group_by_handler(cursor, mariadb, command)

def property_handler(cursor, mariadb, propertyID, command):
      match command:
        case "t":
          print(stats.get_total_entries(cursor, mariadb, propertyID))
        case "a":
          print(stats.get_average_value(cursor, mariadb, propertyID))
        case "n":
          data = stats.get_minimum_value(cursor, mariadb, propertyID)
          print(f"value: {data[3]}, timestamp: {data[2]}")
        case "m":
          data = stats.get_maximum_value(cursor, mariadb, propertyID)
          print(f"value: {data[3]}, timestamp: {data[2]}")
        case _:
          print(command)

def group_by_handler(cursor, mariadb, command):
      match command:
        case "t":
          data = stats.get_group_by_total_entries(cursor, mariadb)
          group_by_printer(data, "Total")
        case "a":
          data = stats.get_group_by_average_value(cursor, mariadb)
          group_by_printer(data, "Average")
        case "n":
          data = stats.get_group_by_minimum_value(cursor, mariadb)
          group_by_printer(data, "Minimum")
        case "m":
          data = stats.get_group_by_maximum_value(cursor, mariadb)
          group_by_printer(data, "Maximum")
        case _:
          print(command)

def group_by_printer(data, column_name):
  for datum in data:
    print(f"ID: {datum[0]}, Name: {datum[1]}, {column_name}: {datum[2]}")