# Напишите программу, в которой пользователь сможет ввести
# временной промежуток в виде количества дней, часов, минут и
# секунд и узнать общее количество секунд, составляющее введенный
# отрезок.

minutes = int(input("Minutes: "))
hours = int(input("Hours: "))
day = int(input("Days: "))



sec = minutes * 60 + hours * 60 * 60 + day * 24 * 60 * 60
print(sec)