# Lab 5: Resistor color code

COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "gray": 8,
    "white": 9
}


def band_value(bands):
    tens = COLORS[bands[0]]
    ones = COLORS[bands[1]]
    multiplier = COLORS[bands[2]]
    return (tens * 10 + ones) * 10 ** multiplier


print(band_value(["brown", "black", "red"]))

