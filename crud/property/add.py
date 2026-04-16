from utils import execute


def add_property(property):
    execute(
        "INSERT INTO property (code,name,location) VALUES (?, ?, ?)",
        (property["code"], property["name"], property["location"])
    )


def request_property():
    print("Give details of a property to add in a semi-colon (;) seperated list in the format: code; name; location")
    print("e.g: 091-010-0669-0001; 2418 Päiväkoti Ariel; 2418 Päiväkoti Ariel")

    user_input = input().split(';')

    property = {
        "code": user_input[0].strip(),
        "name": user_input[1].strip(),
        "location": user_input[2].strip()
    }

    return property


def commit_property_add(connection, property):
    while (1):
        print(
            f"Property with values - code: {property["code"]}, name: {property["name"]}, location: {property["location"]}")
        print(
            "Is ready to commit, please press [Y] to commit or [N] to rollback")
        print()

        user_input = input().lower()

        match user_input:
            case "y":
                print("Committing...")
                connection.commit()
                break
            case "n":
                print("Rolling back...")
                connection.rollback()
                break
            case _:
                print("Command not recognised")
