import numpy as np


def next_term(x):
    return x + ((0.05 - x / 20) * np.cos(10 * x) + (1 / 20) * np.sin(10 * x) - 0.03) / (
        10 * np.sin(10 * x) * (0.05 - x / 20)
    )


x = 0.05
tolerance = x
n = 0
while tolerance > 10 ** (-4):
    n += 1
    x2 = next_term(x)
    tolerance = abs(x2 - x)
    x = x2
    print(f"{n}&{format(x,"1.6f")}&{format(tolerance,"1.6f")}")
