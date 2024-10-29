u = int(input())
f = ""
for i in range(u):
    s = input()
    if len(s) >= 10:
        d = s[0] + str(len(s)-2) + s[-1]
    else:
        d = s
    f += d + '\n'
print(f)