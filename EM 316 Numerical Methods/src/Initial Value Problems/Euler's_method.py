h = 0.5
t0 = 0
y0 = 1


def f(y, t):
    return y * t**2 - 1.1 * y


y = y0
t = t0
while t <= 2:
    y = y + h * f(y, t)
    t += h

print(y)
