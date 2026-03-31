import mariadb
from connector import cursor

def execute(sql_statement, values="", limit=False):
  if limit:
    sql_statement += " LIMIT 1"
  try:
    cursor.execute(sql_statement, values)
  except mariadb.Error as e:
    print(f"Error: {e}")