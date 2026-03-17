def get_total_entries(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT COUNT(*) FROM electricity WHERE property={propertyID}")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data[0]

def get_group_by_total_entries(cursor, mariadb):
  try:
    cursor.execute("""
                    SELECT property.id, property.name, COUNT(electricity.value) as total 
                    FROM electricity 
                    LEFT JOIN property
                    ON electricity.property = property.id
                    GROUP BY property
                  """)
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def get_average_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT AVG(value) FROM electricity WHERE property={propertyID}")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return round(data[0], 3)

def get_group_by_average_value(cursor, mariadb):
  try:
    cursor.execute("""
                    SELECT property.id, property.name, AVG(electricity.value) as total 
                    FROM electricity 
                    LEFT JOIN property
                    ON electricity.property = property.id
                    GROUP BY property
                  """)
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def get_minimum_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT * FROM electricity WHERE value = (SELECT min(value) FROM electricity WHERE property={propertyID})")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data

def get_group_by_minimum_value(cursor, mariadb):
  try:
    cursor.execute("""
                    SELECT property.id, property.name, MIN(electricity.value) as total 
                    FROM electricity 
                    LEFT JOIN property
                    ON electricity.property = property.id
                    GROUP BY property
                  """)
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data

def get_maximum_value(cursor, mariadb, propertyID):
  try:
    cursor.execute(f"SELECT * FROM electricity WHERE value = (SELECT max(value) FROM electricity WHERE property={propertyID})")
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchone()
  return data

def get_group_by_maximum_value(cursor, mariadb):
  try:
    cursor.execute("""
                    SELECT property.id, property.name, MAX(electricity.value) as total 
                    FROM electricity 
                    LEFT JOIN property
                    ON electricity.property = property.id
                    GROUP BY property
                  """)
  except mariadb.Error as e:
    print(f"Error: {e}")
  
  data = cursor.fetchall()
  return data