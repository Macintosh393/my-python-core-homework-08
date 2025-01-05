from datetime import date, datetime, timedelta
from copy import deepcopy


def get_birthdays_per_week(users):
    users = deepcopy(users) # копія вхідного списку
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] # дні тижня для складання вихідного словника
    result = {} # вихідний словник

    if len(users) == 0: # випадок коли було отримано пустий список
        return result

    for i in range (7): # ітерація вздовж тижня включаючи сьогоднішній день
        for person in users:
            cur_date = date.today() + timedelta(days=i) # дата в поточній ітерації

            if (person['birthday'].month, person['birthday'].day) == (cur_date.month, cur_date.day): # порівняння поточної дати з датою дня народження
                if cur_date.weekday() == 5 or cur_date.weekday() == 6: # випадок якщо день народження припадає на вихідні
                    result['Monday'] = result.get('Monday', []) + [person['name']] # привітання переноситься на понеділок
                else:
                    result[days_of_week[cur_date.weekday()]] = result.get(days_of_week[cur_date.weekday()], []) + [person['name']] # у вихідному словнику, до списку, що асоціюється з ключем, що відповідає дню тижня, додаємо імена людей у кого в цей день - день народження

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
