def func(x):
    fx = x**2/(10+x**3)
    return fx

a = int(input("a: "))
b = int(input("b: "))
N = 100
width = (b-a)/N

f = []

i = a

while i <= b:
    f.append(func(i))
    i += width

sum = 0

for i in range(len(f)):
    if i == 0:
        sum += (width/2)*func(a)
    elif i == len(f):
        sum += (width/2)*func(b)
    else:
        sum += width*f[i]

print(f"{sum:.5f}")