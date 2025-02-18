import datetime

def get_days_from_today(date: datetime.date) -> int:
    today = datetime.date.today()
    return (today - datetime.date.fromisoformat(date)).days

# * Test

# print(get_days_from_today('2025-01-01'))