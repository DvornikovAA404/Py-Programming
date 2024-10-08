s = input("Enter a string: ")
if not (s[:3].isdigit()) and (s[:3].isupper()) and s[3:].isdigit():
    print("OLD")
elif s[:4].isdigit() and not(s[4:].isdigit()) and s[4:].isupper():
    print("NEW")
else:
    print("DOES NOT MATCH THE FORMAT")