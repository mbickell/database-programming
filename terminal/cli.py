import argparse
from terminal.property import begin_property_cli 

def begin_cmd(cursor, connection, mariadb):
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--file')

  args = parser.parse_args()
  
  print()
  if (args.file):
      print(args)
  else:
      begin_property_cli(cursor, connection, mariadb)


