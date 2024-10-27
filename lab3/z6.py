s = input("Enter a cipher: ")
if s[-1] == "#":
    s1 = list(s)
    s1.pop()
    s2 = s1
    for i in range(1, len(s1)-1):
        s2[i] = s[i+1]
    s2[-1] = s[1]
    print(''.join(s2))
else:
    print("This is not a code!")