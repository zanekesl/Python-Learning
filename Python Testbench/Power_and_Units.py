# Lab 2: Power

def power_vi(v, i):
    return(i * v)

def power_vr(v, r):
    return((v ** 2) / r)
    
def to_milliwatts(watts):
    mw = 1e3 * watts
    return(1e3 * watts)

print(power_vr(5, 220))
print(to_milliwatts(5))
