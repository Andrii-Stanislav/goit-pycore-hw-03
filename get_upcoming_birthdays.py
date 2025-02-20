from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict: {"name": str, "birthday": str}]) -> list[dict: {"name": str, "congratulation_date": str}]:
    today = datetime.today()
    
    upcoming_birthdays = []
            
    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d")
        this_year_birthday_date = datetime.today().replace(day=birthday.day, month=birthday.month)

        
        if (this_year_birthday_date >= today and abs(this_year_birthday_date - today) <= timedelta(days=7)):            
            congratulation_date = this_year_birthday_date
            
            if (this_year_birthday_date.timetuple().tm_wday == 5): 
                congratulation_date = this_year_birthday_date + timedelta(days=2)
            
            if (this_year_birthday_date.timetuple().tm_wday == 6): 
                congratulation_date = this_year_birthday_date + timedelta(days=1)
            
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays 

users = [
    {"name": "Mary Jane", "birthday": "1985.02.10"},
    {"name": "Sam Smith", "birthday": "1986.02.20"},
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Jane Smith", "birthday": "1990.02.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
