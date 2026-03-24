from utils import execute

def group_by_query_builder(specific_query):
  initial_query = "SELECT property.code, property.name, "
  final_query = """
                \nFROM electricity 
                LEFT JOIN property
                ON electricity.property = property.id
                GROUP BY property
                """
  return initial_query + specific_query + final_query


def get_total_entries(cursor, propertyID):
  execute(f"SELECT COUNT(*) FROM electricity WHERE property={propertyID}")
  
  data = cursor.fetchone()
  return data[0]

def get_group_by_total_entries(cursor):
  execute(group_by_query_builder("COUNT(electricity.value) as total"))
  
  data = cursor.fetchall()
  return data

def get_average_value(cursor, propertyID):
  execute(f"SELECT AVG(value) FROM electricity WHERE property={propertyID}")
  
  data = cursor.fetchone()
  return round(data[0], 3)

def get_group_by_average_value(cursor):
  execute(group_by_query_builder("AVG(electricity.value) as average"))
  
  data = cursor.fetchall()
  return data

def get_minimum_value(cursor, propertyID):
  execute(f"SELECT value, timestamp FROM electricity WHERE value = (SELECT min(value) FROM electricity WHERE property={propertyID})")
  
  data = cursor.fetchone()
  return data

def get_group_by_minimum_value(cursor):
  execute(group_by_query_builder("electricity.timestamp, MIN(electricity.value) as minimum"))
  
  data = cursor.fetchall()
  return data

def get_maximum_value(cursor, propertyID):
  execute(f"SELECT value, timestamp FROM electricity WHERE value = (SELECT max(value) FROM electricity WHERE property={propertyID})")
  
  data = cursor.fetchone()
  return data

def get_group_by_maximum_value(cursor):
  execute(group_by_query_builder("electricity.timestamp, MAX(electricity.value) as maximum"))
  
  data = cursor.fetchall()
  return data