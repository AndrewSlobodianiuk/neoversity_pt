import pathlib
import sys
from pathlib import Path

from colorama import Fore, init

current_dir = pathlib.Path(__file__).parent
init(autoreset=True)


def total_salary(file_name):
    try:
        with open(current_dir / file_name, "r", encoding="utf-8") as file:
            salaries = []

            for line in file:
                parsed_line = line.strip().split(",")

                salaries.append(int(parsed_line[1]))

            total = sum(salaries)
            return (total, total / len(salaries))

    except FileNotFoundError:
        print("File not found.")
        return (0, 0)

    except Exception as e:
        print(f"Something went wrong: {e}")
        return (0, 0)


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


def get_cats_info(file_name):
    try:
        with open(current_dir / file_name, "r", encoding="utf-8") as file:
            cats = []

            for line in file:
                parsed_line = line.strip().split(",")

                cats.append(
                    {
                        "id": parsed_line[0],
                        "name": parsed_line[1],
                        "age": parsed_line[2],
                    }
                )

            return cats

    except FileNotFoundError:
        print("File not found.")
        return (0, 0)

    except Exception as e:
        print(f"Something went wrong: {e}")
        return (0, 0)


cats_info = get_cats_info("cats.txt")
print(cats_info)


def print_directory_structure(path: Path, indent: str = ""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                print_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Permission Denied] {item}")


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Помилка: Необхідно передати шлях до директорії як аргумент.")
        print("Приклад: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{input_path}' не існує.")
        sys.exit(1)

    if not input_path.is_dir():
        print(f"{Fore.RED}Помилка: '{input_path}' не є директорією.")
        sys.exit(1)

    print(f"{Fore.YELLOW}Вміст директорії: {input_path}\n")
    print_directory_structure(input_path)


if __name__ == "__main__":
    main()
