n = input("Enter a number: ")
exp = 0
dec = 0
for i in range(len(n)-1, -1, -1):
    if n[i] == '1':
       dec = dec + 2 ** exp
    exp = exp + 1

print(dec)