from tabulate import tabulate
from crud.views.report import (
    get_3_day_moving_average,
    get_average_daily,
    get_daily_ranking,
    get_detected_anomalies,
    get_full_report,
    get_highest_daily,
    get_most_energy_intensive,
    get_total_consumption
)

options = [
    "Total Consumption per Property",
    "Most Energy-Intensive Property",
    "Average Daily Consumption",
    "Full Report",
    "Detect Anomalies",
    "Highest Daily Consumption",
    "Daily Ranking",
    "3-Day Moving Average"
]


def begin_report_cli(cursor):
    print("Welcome to the reporting cli")
    print("Please select your operation from the list below:\n")

    while (1):
        index = 1
        for option in options:
            print("[" + str(index) + "]: " + option)
            index += 1

        print("[B]ack\n")

        command = input().lower()

        print()

        match(command):
            case "1":
                data = get_total_consumption(cursor)
                print(tabulate(data, headers=[
                      "Name", "Total (kWh)"], floatfmt=".4f"))
            case "2":
                data = get_most_energy_intensive(cursor)
                print(tabulate([data], headers=[
                      "Name", "Total (kWh)"], floatfmt=".4f"))
            case "3":
                data = get_average_daily(cursor)
                print(tabulate(data, headers=[
                      "Name", "Daily Average (kWh)"], floatfmt=".4f"))
            case "4":
                data = get_full_report(cursor)
                print(tabulate(data, headers=[
                    "Name", "Total (kWh)", "Daily Average (kWh)", "Daily Max (kWh)"], floatfmt=".4f"))
            case "5":
                data = get_detected_anomalies(cursor)
                print(tabulate(data, headers=[
                    "Name", "Timestamp", "Value"], floatfmt=".4f"))
            case "6":
                data = get_highest_daily(cursor)
                print(tabulate(data, headers=[
                    "Name", "Day", "Value"], floatfmt=".4f", ))
            case "7":
                data = get_daily_ranking(cursor)
                print(tabulate(data, headers=[
                    "Timestamp", "Name", "Value", "Rank Position"], floatfmt=".4f", ))
            case "8":
                data = get_3_day_moving_average(cursor)
                print(tabulate(data, headers=[
                    "Name", "Timestamp", "3-Day Average"], floatfmt=".4f", ))
            case "b":
                break
            case _:
                print("Command not recognised")

        print()
