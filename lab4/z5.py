s = ([int(l) for l in input("Student height: ").split()])
y = int(input("Your height: "))

s.append(y)
s.sort(reverse=True)
print(s.index(y)+1)