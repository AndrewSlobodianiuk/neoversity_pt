def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
        except KeyError:
            return "Contact doesn't exist"

    return inner


@input_error
def add_contact(name, number, db):
    if name in db:
        return "Contact already exists"
    db[name] = number
    return "Contact added."


@input_error
def find_number_by_name(name, db):
    return db[name]


@input_error
def change_number_by_name(name, number, db):
    db[name] = number
    return "Contact updated."


def log_contacts(db):
    if not db:
        return "No contacts found."
    return "\n".join(f"{k}: {v}" for k, v in db.items())


def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main():
    db = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            print("Enter a command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        match command:
            case "hello":
                print("How can I help you?")

            case "add":
                if len(args) < 2:
                    print("Give me name and phone please.")
                    continue
                name, number = args
                print(add_contact(name, number, db))

            case "phone":
                if len(args) < 1:
                    print("Enter the argument for the command")
                    continue
                print(find_number_by_name(args[0], db))

            case "change":
                if len(args) < 2:
                    print("Give me name and phone please.")
                    continue
                name, number = args
                print(change_number_by_name(name, number, db))

            case "all":
                print(log_contacts(db))

            case _:
                print("Unknown command")


if __name__ == "__main__":
    main()
