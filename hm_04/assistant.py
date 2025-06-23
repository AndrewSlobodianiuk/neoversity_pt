def add_contact(name="", number="", db={}):
    if name in db:
        print("Contact already exist")
        return

    db[name] = number


def find_number_by_name(name="", db={}):
    if name not in db:
        print("Contact doesn't exist")
        return

    return db[name]


def change_number_by_name(name="", number="", db={}):
    if name not in db:
        print("Contact doesn't exist")
        return

    db[name] = number


def log_contacts(db):
    for k, v in db.items():
        print(f"{k}: {v}")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def main():
    db = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        match command:
            case "hello":
                print("How can I help you?")

            case "add":
                name, number = args
                add_contact(name, number, db)

            case "phone":
                print(find_number_by_name(args[0], db))

            case "change":
                name, number = args
                change_number_by_name(name, number, db)

            case "all":
                log_contacts(db)

            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
