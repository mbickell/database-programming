from tabulate import tabulate
import crud.electricity.stats as stats
from crud.property.read import get_property_by_code


def get_property_code(filename):
    start_of_code_index = filename.index("/0") + 1
    end_of_code_index = filename.rindex('.')
    return filename[start_of_code_index:end_of_code_index]


def begin_stats_cli(cursor):
    print(
        "Select your property with it's property code OR enter [G] to group by property")

    user_input = input().lower()
    property_code = None
    propertyID = None

    if user_input != "g":
        property_code = user_input
        propertyID = get_property_by_code(cursor, property_code)[0]

    while (1):
        print()

        if property_code:
            print(
                f"Property with code {property_code} selected, please select your operation")
        else:
            print("Grouping by properties")

        print(
            "[T]otal, [A]verage, Mi[N], [M]ax, Change [P]roperty, Switch to [G]roup by mode, [B]ack")
        command = input().lower()

        print()

        match command:
            case "p":
                print("Select a new property with it's property code")
                property_code = input().lower()
                propertyID = get_property_by_code(cursor, property_code)[0]
            case "g":
                propertyID = None
                property_code = None
            case "b":
                print("Going back...")
                break
            case _:
                if property_code:
                    property_handler(cursor, propertyID, command)
                else:
                    group_by_handler(cursor, command)


def property_handler(cursor, propertyID, command):
    match command:
        case "t":
            print(
                f"Total entries: {stats.get_total_entries(cursor, propertyID)}")
        case "a":
            print(
                f"Average value: {stats.get_average_value(cursor, propertyID)}")
        case "n":
            data = stats.get_minimum_value(cursor, propertyID)
            print(tabulate([data], headers=["Value", "Timestamp"]))
        case "m":
            data = stats.get_maximum_value(cursor, propertyID)
            print(tabulate([data], headers=["Value", "Timestamp"]))
        case _:
            print(command)


def group_by_handler(cursor, command):
    match command:
        case "t":
            data = stats.get_group_by_total_entries(cursor)
            group_by_printer(data, "Total")
        case "a":
            data = stats.get_group_by_average_value(cursor)
            group_by_printer(data, "Average")
        case "n":
            data = stats.get_group_by_minimum_value(cursor)
            group_by_printer(data, "Minimum")
        case "m":
            data = stats.get_group_by_maximum_value(cursor)
            group_by_printer(data, "Maximum")
        case _:
            print(command)


def group_by_printer(data, column_name):
    if len(data[0]) > 3:
        print(tabulate(data, headers=[
              "Code", "Name", "Timestamp", column_name]))
    else:
        print(tabulate(data, headers=[
              "Code", "Name", column_name]))
