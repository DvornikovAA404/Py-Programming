from random import randint
from playsound import playsound

def show(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()

size = 4
playsound("Start.wav", False)

a = []
for i in range(size):
    b = []
    for j in range(size):
        b.append("*")
    a.append(b)

suba = []
for i in range(size):
    subb = []
    for j in range(size):
        subb.append(0)
    suba.append(subb)

i = 0
while i < 4:
    x = randint(0, size-1)
    y = randint(0, size-1)
    if suba[x][y] == 0:
        suba[x][y] = 1
        i+=1

i = 0
while i < 1:
    x = randint(0, size-1)
    y = randint(0, size-1)
    if suba[x][y] == 0:
        suba[x][y] = 2
        i+=1
show(a)
print()

kills = 0
v = 0
while True:
    x = 0
    y = 0
    try:
        pos = input("Enter a position (x, y): ").split(" ")
        x = int(pos[0])-1
        y = int(pos[1])-1
        if suba[x][y] == 0:
            playsound("Vsplesk.wav", False)
            a[x][y] = "Q"
            show(a)
        elif suba[x][y] == 1:
            playsound("Vzriv.wav", False)
            kills += 1
            a[x][y] = "X"
            suba[x][y] = 0
            show(a)
        elif suba[x][y] == 2:
            a[x][y] = "B"
            show(a)
            print("Поражение!")
            playsound("Defeat.wav")
            break
        if kills == 4:
            v = 1
            print("Флот противника уничтожен!")
            playsound("Victory.wav")
            break
    except:
        print("Invalid input")
        continue