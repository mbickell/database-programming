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
                get_total_consumption(cursor)
            case "2":
                get_most_energy_intensive(cursor)
            case "3":
                get_average_daily(cursor)
            case "4":
                get_full_report(cursor)
            case "5":
                get_detected_anomalies(cursor)
            case "6":
                get_highest_daily(cursor)
            case "7":
                get_daily_ranking(cursor)
            case "8":
                get_3_day_moving_average(cursor)
            case "b":
                break
            case _:
                print("Command not recognised")

        print()
