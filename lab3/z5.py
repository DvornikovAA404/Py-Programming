def count_vowels(line):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in line if char in vowels)


def check_haiku(lines):
    if "" in lines:
        return "Не хайку. Должно быть 3 строки."

    syllables = [count_vowels(line) for line in lines]

    if syllables == [5, 7, 5]:
        return "Хайку!"
    else:
        return "Не хайку."


# Вводим строки
lines = []
for i in range(3):
    lines.append(input("Enter the line: "))

# Проверяем хайку
result = check_haiku(lines)
print(result)
