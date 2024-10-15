n = int(input("Enter a count: "))
price = 0
for i in range(n):
    age = int(input("Enter an age: "))
    if age < 2:
        price += 0
    elif 3 <= age < 12:
        price += 100
    elif age > 65:
        price += 120
    else:
        price += 200

print(price)
