from random import *
s = input("Enter 2 words: ")
if len(s.split()) == 2:
    if len(s.split()[0]) < len(s.split()[1]):
        print(s.split()[1][:len(s.split()[0])])
    else:
        print(choice(s.split()))
else:
    print("Ошибка! Некорректное количество слов")