import math
s = input("Enter a string: ")
s1 = s[math.ceil(len(s)/2):] + s[:math.ceil(len(s)/2)]
print(s1)