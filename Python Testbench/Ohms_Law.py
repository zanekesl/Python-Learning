# Lab 1: Ohm's law
# Units: volts, amps, ohms

def voltage(current, resistance):
    voltage = current * resistance
    return(voltage)

def current(voltage, resistance):
    current = voltage / resistance
    return(current)


# Try your functions here before running the checks:
print(voltage(0.02, 220))
print(current(.4, 7373))
