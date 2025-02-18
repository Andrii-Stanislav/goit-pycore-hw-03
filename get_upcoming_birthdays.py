from datetime import datetime, timedelta

# Додаткова функція оскільки одразу трохи не так зрозумів ТЗ
def get_next_week_birthdays(users: list[dict: {"name": str, "birthday": str}]) -> list[dict: {"name": str, "congratulation_date": str}]:
    today = datetime.today()
    today_week_iso = int(today.strftime("%V"))
    
    upcoming_birthdays = []
        
    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d")
        birthday_week_iso_str = birthday.strftime("%V")
        
        if (not birthday_week_iso_str.isdigit()):
            continue
    
        if (today_week_iso + 1 == int(birthday_week_iso_str)):
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": user['birthday']})

    return upcoming_birthdays 
    

def get_upcoming_birthdays(users: list[dict: {"name": str, "birthday": str}]) -> list[dict: {"name": str, "congratulation_date": str}]:
    today = datetime.today().timetuple() # .tm_yday
    
    upcoming_birthdays = []
        
    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d")
        birthday_timetuple = birthday.timetuple()
        
        if (birthday_timetuple.tm_yday >= today.tm_yday and birthday_timetuple.tm_yday - today.tm_yday <= 7):
            this_year_birthday_date = datetime.today().replace(day=birthday.day)
            
            congratulation_date = birthday
            
            if (this_year_birthday_date.timetuple().tm_wday == 5): 
                congratulation_date = birthday + timedelta(days=2)
            
            if (this_year_birthday_date.timetuple().tm_wday == 6): 
                congratulation_date = birthday + timedelta(days=1)
            
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays 

users = [
    {"name": "Mary Jane", "birthday": "1985.02.10"},
    {"name": "Sam Smith", "birthday": "1986.02.20"},
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Jane Smith", "birthday": "1990.02.27"}
]

# next_week_birthdays = get_next_week_birthdays(users)
# print("Список привітань на наступному  тижні:", next_week_birthdays)

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
