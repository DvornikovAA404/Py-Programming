try:
    s = input("Enter a list of numbers: ").split()
except ValueError:
    print("Error!")
a = []
for i in range(1, len(s)):
    if int(s[i] > s[i-1]):
        a.append(s[i])
print(a)