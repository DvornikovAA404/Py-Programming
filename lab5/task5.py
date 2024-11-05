size = input("Укажите размер (n m): ")
x = size.split(" ")[0]
y = size.split(" ")[1]
a = []
for i in range(int(x)):
    b = []
    for j in range(int(y)):
        b.append(str(i+1)+str(j+1))
    a.append(b)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

p = []
for i in range(int(y)):
    pb = []
    for j in range(int(x)):
        pb.append(0)
    p.append(pb)
print()

for i in range(int(x)):
    for j in range(int(y)):
        p[j][i] = a[i][j]

for i in range(len(p)):
    for j in range(len(p[i])):
        print(p[i][j], end=" ")
    print()