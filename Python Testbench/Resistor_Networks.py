# Lab 4: Resistor networks

def series(resistors):
    total_r_s = 0
    for r in resistors:
        total_r_s += r
    return total_r_s

def parallel(resistors):
    total_r_p = 0
    for r in resistors:
        total_r_p += 1 / r
    return 1 / total_r_p


print(series([100, 220, 330]))
print(parallel([10, 10]))