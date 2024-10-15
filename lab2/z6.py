import random

secret = random.randint(1, 10)

print("Хорошо, я загадал число. Попробуй его отгадать")
c = 0
while 1:
    c += 1
    num = int(input(f'{c} '))
    if num == secret:
        print("Поздравляю! Вы угадали!")
        ans = input("Хотите сыграть еще раз? (Yes, no) ")
        if ans.lower() == 'no':
            break
    else:
        print("Нее, ты не угадал. Попробуй снова")
    if num > secret:
        print("Ваше число больше загаданного!")
    elif num < secret:
        print("Ваше число меньше загаданного!")
