a = int(input('AB = '))
b = int(input('BC = '))
c = int(input('AC = '))

if  a == b == c:
    print("Равносторонний")
elif a == b or b == c or a == c:
    print("Равнобедренный")
else:
    print("Разносторонний")