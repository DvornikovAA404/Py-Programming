def show(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()

size = int(input("Enter the size of the array: "))

a = []
for i in range(size):
    b = []
    for j in range(size):
        b.append(int(input(f"[{i}, {j}] : ")))
    a.append(b)
print("==============================")
show(a)

p = []
for i in range(int(size)):
    pb = []
    for j in range(int(size)):
        pb.append(a[i][j])
    p.append(pb)
print()

print("==============================")
show(p)

for i in range(size):
    for j in range(size):
        if i == j:
            p[i][j] = a[size-1-i][j]
            p[size-1-i][j] = a[i][j]

print("==============================")
show(p)