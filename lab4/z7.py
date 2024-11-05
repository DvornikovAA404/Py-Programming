s = input("Enter a number: ")
k = 0
for i in range(len(s)):
    if i%2==0:
        k += int(s[i])
for i in range(len(s)):
    if i%2!=0:
        u = 9 if int(s[i])*2 > 9 else 0
        k += int(s[i]) * 2 - u
if k%10==0:
    print("Incorrect!")
else:
    print("Correct!")