n = int(input('Enter a number: '))
a = range(1, n+1)
y = 0
for i in range(n):
    y += a[i] * a[i]

print(y)
