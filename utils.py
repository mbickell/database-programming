import mariadb
from connector import cursor

def execute(sql_statement, values=""):
  try:
    cursor.execute(sql_statement, values)
  except mariadb.Error as e:
    print(f"Error: {e}")