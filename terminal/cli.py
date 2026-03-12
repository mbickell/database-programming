import argparse
from terminal.property import begin_property_cli 
from terminal.electricty import get_property_code
from crud.property.read import get_property
from crud.property.add import add_property
from crud.electricity.add import read_json_data

def begin_cmd(cursor, connection, mariadb):
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--file')

  args = parser.parse_args()
  
  if (args.file):
    code = get_property_code(args.file)
    exists = len(get_property(cursor, mariadb, code)) > 0
    print(exists)
    if exists:
      print("Property already exists")
    else:
      electricity_data = read_json_data(args.file)
      location_name = electricity_data[0]["locationName"]
      print({"code": code, "name": location_name, "location": location_name})
      # add_property(cursor, mariadb, {"code": code, "name": location_name, "location": location_name})
      property_id = get_property(cursor, mariadb, code)[0]["id"]
      # Insert the electricity data
      return
  else:
    begin_property_cli(cursor, connection, mariadb)


