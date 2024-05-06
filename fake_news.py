from datetime import datetime
day = ['день', "дня", "дней"]
hour = ['час', 'часа', 'часов']
minute = ['минута', 'минуты', 'минут']
def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return str(amount) + ' ' + declensions[0]
    elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        return str(amount) + ' ' + declensions[1]
    else:
        return str(amount) + ' ' + declensions[2]

current_datetime = input()
current_date = datetime.strptime(current_datetime, '%d.%m.%Y %H:%M')
course_date = datetime(2022, 11, 8, 12, 0)
time_until_course = course_date - current_date

days = time_until_course.days

# Остаток секунд после вычитания целых дней
seconds_remainder = time_until_course.seconds

hours = seconds_remainder // 3600
minutes = (seconds_remainder % 3600) // 60

if days > 0 and hours == 0:
    print(f"До выхода курса осталось: {choose_plural(time_until_course.days, day)}")
elif days > 0 and hours > 0:
    print(f"До выхода курса осталось: {choose_plural(time_until_course.days, day)} и {choose_plural(time_until_course.seconds // 3600, hour)}")
elif time_until_course.seconds > 0 and minutes == 0:
    print(f"До выхода курса осталось: {choose_plural(time_until_course.seconds // 3600, hour)}")
elif hours == 0 and days == 0 and minutes > 0:
    print(f"До выхода курса осталось: {choose_plural((time_until_course.seconds % 3600) // 60, minute)}")
elif days == 0 and time_until_course.seconds > 0:
    print(f"До выхода курса осталось: {choose_plural(time_until_course.seconds // 3600, hour)} и {choose_plural((time_until_course.seconds % 3600) // 60, minute)}")

else:
    print("Курс уже вышел!")
