number = input("Enter a number: ")
a = 0
b = 0
if len(number) == 6:
    for i in range(len(number)//2):
        a += int(number[i])
    for i in range(len(number)//2, len(number)):
        b += int(number[i])

    if a == b:
        print("Ваше число счастливое!")
    else:
        print("Обычный билет")
else:
    print("Некорректный билет")