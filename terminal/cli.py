import argparse
from terminal.property import begin_property_cli 
from terminal.electricty import get_property_code
from crud.property.read import get_property_by_code
from crud.property.add import add_property
from crud.electricity.add import read_json_data, insert_electricity

def begin_cmd(cursor, connection):
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--file')

  args = parser.parse_args()
  
  if (args.file):
    code = get_property_code(args.file)
    exists = len(get_property_by_code(cursor, code)) > 0

    if exists:
      print("Property already exists")
    else:
      electricity_data = read_json_data(args.file)
      location_name = electricity_data[0]["locationName"]
      
      add_property({"code": code, "name": location_name, "location": location_name})
      connection.commit()

      property_id = get_property_by_code(cursor, code)[0][0]
      insert_electricity(connection, electricity_data, property_id)
      print("Property and electricity data added")
  else:
    begin_property_cli(cursor, connection)


