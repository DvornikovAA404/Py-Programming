import string
import random

length = int(input("Enter a length: "))
a = []
if input("Need capital letters?(Y/N)")=="Y":
    a.extend(string.ascii_uppercase)
if input("Need lowercase letters?(Y/N)")=="Y":
    a.extend(string.ascii_lowercase)
if input("Need numbers?(Y/N)")=="Y":
    a.extend(string.digits)
if input("Need symbols?(Y/N)")=="Y":
    a.extend(string.punctuation)
print(''.join([random.choice(a) for n in range(length)]))