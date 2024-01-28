import numpy as np


def f(x):
    return np.exp(-(x**2))


a = 0
b = 1

N = 100000
h = (b - a) / N
answer = 0
for i in range(N + 1):
    if i == 0 or i == N:
        answer += 2 * h * f(a + i / N)
    else:
        answer += h * f(a + i / N)

print(answer)
