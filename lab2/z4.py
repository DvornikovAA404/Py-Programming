height = int(input('Enter your height: '))

for i in range(height):
    ch = 1 + (i * 2)
    sp = height - i
    print(' '*sp+'#'*ch)
print(' '*height+'#')