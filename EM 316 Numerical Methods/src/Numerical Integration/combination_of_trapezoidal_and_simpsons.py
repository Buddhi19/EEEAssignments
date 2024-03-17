import numpy as np
from scipy import integrate

X = [1, 2, 3.25, 4.5, 6, 7, 8, 9, 9.5, 10]

Y = [5, 6, 5.5, 7, 8.5, 8, 6, 7, 7, 5]

Trapezoidal = []
Simpsons = []

X = [x * 60 for x in X]  # convert to seconds

from collections.abc import Sequence


def simpson_nonuniform(x: Sequence[float], f: Sequence[float]) -> float:
    N = len(x) - 1
    h = [x[i + 1] - x[i] for i in range(0, N)]
    assert N > 0

    result = 0.0
    for i in range(1, N, 2):
        h0, h1 = h[i - 1], h[i]
        hph, hdh, hmh = h1 + h0, h1 / h0, h1 * h0
        result += (hph / 6) * (
            (2 - hdh) * f[i - 1] + (hph**2 / hmh) * f[i] + (2 - 1 / hdh) * f[i + 1]
        )

    if N % 2 == 1:
        h0, h1 = h[N - 2], h[N - 1]
        result += f[N] * (2 * h1**2 + 3 * h0 * h1) / (6 * (h0 + h1))
        result += f[N - 1] * (h1**2 + 3 * h1 * h0) / (6 * h0)
        result -= f[N - 2] * h1**3 / (6 * h0 * (h0 + h1))
    return result


print(simpson_nonuniform(X, Y) / 60)
