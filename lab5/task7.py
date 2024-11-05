
from random import randint

def show(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()

size = input("Enter the size of the array: ")
x = size.split(" ")[0]
y = size.split(" ")[1]

a = []
for i in range(int(x)):
    b = []
    for j in range(int(y)):
        b.append(randint(0,1))
    a.append(b)
show(a)

gr = int(input("Enter the group size: "))


for i in range(len(a)):
    s = 0
    for j in range(len(a[i])):
        if a[i][j] == 1:
            s += 1
    if s >= gr:
        print(i+1)
        break
else:
    print(0)
