import random
import re
from datetime import datetime, timedelta


def get_days_from_today(date):
    current_date = datetime.now().date()
    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    delta = current_date - parsed_date

    return delta.days


def get_numbers_ticket(min, max, quantity):
    return (
        []
        if min < 1 or max > 1000 or quantity > (max - min)
        else sorted(random.sample(range(min, max), k=quantity))
    )


def normalize_phone(phone_number):
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    if cleaned.startswith("+380"):
        return cleaned

    if cleaned.startswith("380"):
        return "+" + cleaned

    return "+38" + cleaned.lstrip("+")


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1988.03.15"},
    {"name": "Bob Williams", "birthday": "1979.07.09"},
    {"name": "Clara Brown", "birthday": "1992.12.04"},
    {"name": "David Davis", "birthday": "1983.05.30"},
    {"name": "Ella Martinez", "birthday": "1995.09.22"},
    {"name": "Frank Miller", "birthday": "1981.11.18"},
    {"name": "Grace Wilson", "birthday": "1993.04.05"},
    {"name": "Henry Moore", "birthday": "1987.02.12"},
    {"name": "Isla Taylor", "birthday": "1991.06.25"},
    {"name": "Jack Anderson", "birthday": "1980.10.14"},
    {"name": "Kara Thomas", "birthday": "1984.08.19"},
    {"name": "Liam Jackson", "birthday": "1989.01.03"},
    {"name": "Mia White", "birthday": "1994.07.17"},
    {"name": "Noah Harris", "birthday": "1986.09.28"},
    {"name": "Olivia Martin", "birthday": "1996.12.11"},
    {"name": "Paul Thompson", "birthday": "1982.03.06"},
    {"name": "Quinn Garcia", "birthday": "1997.11.02"},
    {"name": "Ruby Clark", "birthday": "1990.05.21"},
    {"name": "Sam Lewis", "birthday": "1985.04.08"},
    {"name": "Tina Lee", "birthday": "1988.02.27"},
    {"name": "Tina Lee 1", "birthday": "1988.06.21"},
    {"name": "Tina Lee 1", "birthday": "1988.06.17"},
    {"name": "Tina Lee 2", "birthday": "1988.11.30"},
]


def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    schedule = []

    for user in users:
        user_birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = user_birthday_date.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

        days_until_birthday = (birthday_this_year - current_date).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            schedule.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return schedule


print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
