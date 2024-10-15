price = 0
while 1:
    age = int(input("Enter an age: "))
    if age == 0:
        break
    elif age < 2:
        price += 0
    elif 3 <= age < 12:
        price += 100
    elif age > 65:
        price += 120
    else:
        price += 200

print(price)
