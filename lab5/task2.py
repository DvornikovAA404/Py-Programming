from random import *

def show(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()

while True:
    a = []
    for i in range(3):
        b = []
        for j in range(3):
            b.append(randint(0,9))
        a.append(b)
    sumsa = []
    sumsb = []
    sumsd = []
    sum_b = 0
    sum_d = 0
    sum_id = 0
    for i in range(len(a)):
        sum_a = 0
        for j in range(len(a[i])):
            sum_a += a[i][j]
            if j == i:
                sum_d += a[i][i]
        sumsa.append(sum_a)
    for i in range(len(a)):
        sum_b = 0
        for j in range(len(a[i])):
            sum_b += a[j][i]
        sumsb.append(sum_b)
    sum_id = a[0][2] + a[1][1] + a[2][0]
    if sumsa[0] == sumsa[1] == sumsa[2] == sumsb[0] == sumsb[1] == sumsb[2] == sum_d == sum_id:
        show(a)
        print('a:', sumsa)
        print('b:', sumsb)
        print('d:', sum_d)
        print('id:', sum_id)
        break