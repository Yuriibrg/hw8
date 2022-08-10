from datetime import datetime
from datetime import timedelta
from collections import defaultdict

users = {
    "Jack": datetime(year=1967, month=3, day=15),
    "Monica": datetime(year=1976, month=8, day=12),
    "Ivan": datetime(year=1983, month=8, day=10),
    "Rich": datetime(year=1978, month=8, day=14),
}

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_birthdays_per_week():

    today = datetime.now()
    days_of_weeks = defaultdict(list)

    if today.weekday() < 5: #  если сегодня не виходной
        days = [day for day in range(today.weekday(), 5)] # создай список будних дней
    else:
        days = [day for day in range(0, 5)]
    for _ in days:
        days_of_weeks[_]

    for name, birthday in users.items():
        if (birthday.day, birthday.month) == (today.day, today.month):
            if today.weekday() <5:
                days_of_weeks[today.weekday()].append(name)
            else:
                days_of_weeks[0].append(name)

    for _, name_of_birthday in days_of_weeks.items():
        day_of_week = days_of_week[_]
        print(f"{day_of_week}: {', '.join(name_of_birthday)}")

get_birthdays_per_week()





