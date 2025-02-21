from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        this_year_birthday = birthday.replace(year=today.year)

        # If birthday is in the past, move it to next year
        if this_year_birthday < today:
            this_year_birthday = this_year_birthday.replace(year=today.year + 1)

        # Check if birthday is in the next 7 days
        if 0 <= (this_year_birthday - today).days <= 7:
            congratulation_date = this_year_birthday

            # If birthday is on Saturday or Sunday, move it to Monday
            if congratulation_date.weekday() == 5:  # Sateday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "Mary Jane", "birthday": "1985.01.01"},
    {"name": "Sam Smith", "birthday": "1986.02.20"},
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Jane Smith", "birthday": "1990.02.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
