import argparse
from terminal.property import begin_property_cli 
from terminal.electricty import get_property_code
from crud.property.read import check_property_exists

def begin_cmd(cursor, connection, mariadb):
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--file')

  args = parser.parse_args()
  
  if (args.file):
    code = get_property_code(args.file)
    print(check_property_exists(cursor, mariadb, code))
  else:
    begin_property_cli(cursor, connection, mariadb)


