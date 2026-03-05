def list_propeties(cursor, mariadb):
  try:
    cursor.execute("SELECT * FROM property")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def begin_cmd():
  while(1):
    print("Select your operation ([L]ist, [A]dd, [D]elete, e[X]it)")
    command = input().lower()

    match command:
      case "l":
        print("Recived L")
      case "a":
        print("Recived A")
      case "d":
        print("Recived D")
      case "x":
        print("Exiting")
        break
      case _:
        print(command)