age = int(input("Enter age: "))
dog = 0
if age > 0:
    for i in range(1, age+1):
        if i <= 2:
            dog += 10.5
        else:
            dog += 4
    print(dog)
else:
    print('Error!')