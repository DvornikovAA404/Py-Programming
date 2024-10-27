s = input("Enter a string: ")
sp = s.split()
if len(sp) == 2:
    print(sp[1] + ' ' + sp[0])
else:
    print("Ошибка! Некорректное количество слов")