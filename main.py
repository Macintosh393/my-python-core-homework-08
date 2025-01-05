from datetime import date, datetime, timedelta
from copy import deepcopy


def get_birthdays_per_week(users):
    users = deepcopy(users)
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    result = {}

    for i in range (7):
        for person in users:
            cur_date = date.today() + timedelta(days=i)

            if (person['birthday'].month, person['birthday'].day) == (cur_date.month, cur_date.day):
                if cur_date.weekday() == 5 or cur_date.weekday() == 6:
                    result['Monday'] = result.get('Monday', []) + [person['name']]
                else:
                    result[days_of_week[cur_date.weekday()]] = result.get(days_of_week[cur_date.weekday()], []) + [person['name']]

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
