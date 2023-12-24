import numpy as np

e = 0.8
M = 3
TOLERANCE = 10 ** (-4)


def next_term(x):
    return x - (x - e * np.sin(x)) / (1 - e * np.cos(x))


def shape(num):
    return format(num, ".5f")


x = 5
while True:
    temp = x
    x = next_term(x)
    print(f"x={shape(temp)} tolerance={shape(abs(temp-x))}")
    if abs(temp - x) < TOLERANCE:
        break
