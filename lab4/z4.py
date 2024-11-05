s = [int(l) for l in input("Enter a list of numbers: ").split()]
Average = sum(s)/len(s)

b = [i for i in s if i < Average]
c = [i for i in s if i == Average]
d = [i for i in s if i > Average]
print("AVG:", Average)
print("x<AVG: ", b)
if not(c == []):
    print("x = AVG: ", c)
print("x > AVG: ", d)
