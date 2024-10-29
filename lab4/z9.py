a = []
for i in range(int(input("Rooms: "))):
    a.append(input("").split())

k = 0
for i in range(len(a)):
    if int(a[i][1]) - int(a[i][0]) >= 2:
        k += 1
print(k)