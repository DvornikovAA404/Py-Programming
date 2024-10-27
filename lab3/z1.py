s = input("Enter a text: ")
i = s.split()
print(i)
x = len(i)
a = []
for o in range(x):
   if i[o] != i[o-1]:
       a.append(i[o])
print(''.join([s+' ' for s in a]))