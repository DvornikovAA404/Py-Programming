from cgi import print_environ_usage

from prettytable import PrettyTable

def finder(arr, filter):
    for i in range(len(arr)):
        if arr[i][0].lower() == filter.lower():
            table = PrettyTable()
            table.field_names = ["Блюдо", "Ингредиенты", "Цена"]
            table.add_row([menu[i][0], ', '.join([s for s in menu[i][1]]), menu[i][2]])
            print(table)
            return 0
    print("Блюдо не найдено!")


menu = [
["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]


def upd_table(menu):
    table = PrettyTable()
    table.field_names = ["Блюдо", "Ингредиенты", "Цена"]
    for i in range(0, len(menu)):
        table.add_row([menu[i][0], ', '.join([s for s in menu[i][1]]), menu[i][2]])

    print(table)
    print()

upd_table(menu)
while True:
    cmd = input("Find/Add/Change/Quit >> ")
    if cmd == "Find":
        x = input("Название: ")
        finder(menu, x)
    elif cmd == "Add":
        name = input("Введите название блюда: ")
        ingr = input("Введите ингредиенты(Через запятую с пробелом!): ")
        cost = int(input("Введите цену: "))
        menu.append([name, ingr.split(", "), cost])
        print("===Таблица обновлена!===")
        upd_table(menu)
    elif cmd == "Change":
        name = input("Введите название блюда: ")
        cost = int(input("Введите новую цену: "))
        for i in range(0, len(menu)):
            if menu[i][0].lower() == name.lower():
                menu[i][2] = cost
        print("===Таблица обновлена!===")
        upd_table(menu)
    elif cmd == "Quit":
        break
    else:
        print("Неверная команда!")
