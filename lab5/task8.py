def show(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j != 0:
                print(" "*(6-len(str(a[i][j]))), end="")
            print(a[i][j], end="")

        print()

size = input("Enter the size of the array: ")
x = size.split(" ")[0]
y = size.split(" ")[1]

a = []
for i in range(int(x)):
    b = []
    for j in range(int(y)):
        if i == 0 or j == 0:
            b.append(1)
        else:
            b.append(0)
    a.append(b)

for i in range(int(x)):
    for j in range(int(y)):
        if i != 0 and j != 0:
            a[i][j] = a[i-1][j]+a[i][j-1]
show(a)