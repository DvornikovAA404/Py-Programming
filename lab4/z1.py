a = input("Enter elements: ").split()

b = []
c = []

b = [i for i in a if i.isdigit()]
c = [i for i in a if i.isalpha()]

a.clear()
print('Numbers: ', b, '\nDigits: ', c)