from utils import execute
from tabulate import tabulate


def read_properties(cursor):
    execute("SELECT code, name, location FROM property")

    data = cursor.fetchall()
    return data


def print_properties(cursor):
    data = read_properties(cursor)

    print(tabulate(data, headers=["Code", "Name", "Location"]))


def get_property_by_code(cursor, property_code):
    execute(
        f"SELECT id, code, name, location FROM property WHERE code=\"{property_code}\"")

    data = cursor.fetchone()
    return data
