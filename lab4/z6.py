from random import *
step = 0
log = ""
p = 0
while True:
    s = choice("ОР")
    step += 1
    log = log + s
    if s == "Р":
        p += 1
    else:
        p = 0
    if p == 3:
        print(" ".join(log) + f"(попыток: {step})")
        break
