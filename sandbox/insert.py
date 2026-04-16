# retrieve data
def read_data(cursor, mariadb):
    try:
        cursor.execute("SELECT * FROM electricity")
    except mariadb.Error as e:
        print(f"Error: {e}")

    data = cursor.fetchall()

    # print content
    for datum in data:
        print(
            f"id: {datum[0]}, property: {datum[1]} timestamp: {datum[2]}, value: {datum[3]}")
