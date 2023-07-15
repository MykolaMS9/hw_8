from datetime import datetime, timedelta


users = [
    {'name': 'Nick3', 'birthday': datetime(year=1999, month=7, day=15)},
    {'name': 'Nick1', 'birthday': datetime(year=1999, month=7, day=16)},
    {'name': 'Oleg1', 'birthday': datetime(year=1999, month=7, day=16)},
    {'name': 'Nick2', 'birthday': datetime(year=1999, month=7, day=17)},
    {'name': 'Oleg2', 'birthday': datetime(year=1999, month=7, day=18)},
    {'name': 'Mykola', 'birthday': datetime(year=1999, month=7, day=20)},
    {'name': 'Simon', 'birthday': datetime(year=1999, month=7, day=20)},
    {'name': 'Andry', 'birthday': datetime(year=1999, month=7, day=21)},
    {'name': 'Olena', 'birthday': datetime(year=1999, month=7, day=22)},
    {'name': 'Lena', 'birthday': datetime(year=1999, month=7, day=23)},
    {'name': 'Lisa', 'birthday': datetime(year=1999, month=7, day=23)},
    {'name': 'Vera', 'birthday': datetime(year=1999, month=7, day=24)},
    {'name': 'Ivan', 'birthday': datetime(year=1999, month=7, day=25)},
    {'name': 'Lila', 'birthday': datetime(year=1999, month=7, day=26)},
]
def check_work_day(date_):
    weekends = ['Saturday', 'Sunday']
    if date_.strftime("%A") not in weekends:
        return True
    else:
        return False

def pirnt_birthday_person(date_, list_):
    print(f'{date_.strftime("%A")} {date_}: {", ".join(list_)}')

def get_birthdays_per_week(users_list):
    date_today = datetime.now().date()
    miss_ = []
    for week_day in range(7):
        birthday_person_list = [i['name'] for i in filter(lambda val:val['birthday'].strftime("%m %d") == date_today.strftime("%m %d"), users_list)]
        if check_work_day(date_today):
            [miss_.append(val) for val in birthday_person_list]
            if miss_:
                pirnt_birthday_person(date_today, miss_)
            miss_ = []
        else:
            [miss_.append(val) for val in birthday_person_list]
        date_today += timedelta(days=1)
get_birthdays_per_week(users)
