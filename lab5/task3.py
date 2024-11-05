import math

count = 4
treasures = [[1,2], [3, 5], [5, 6], [7, 8]]
pos = [5, 0]

a = []

for i in range(count):
    R = math.sqrt((pos[0]-treasures[i][0])**2+(pos[1]-treasures[i][1])**2)
    a.append(R)

P = min(a)

for i in range(count):
    R = math.sqrt((pos[0] - treasures[i][0]) ** 2 + (pos[1] - treasures[i][1]) ** 2)
    if R == P:
        print(treasures[i])
        break