a = []
while 1:
    height = int(input('Enter your height: '))
    if height == 0:
        break
    else:
        a.append(height)
if len(a) > 1:
    print('Max: ', max(a))
    print('Min: ', min(a))
else:
    print('Некого сравнивать')