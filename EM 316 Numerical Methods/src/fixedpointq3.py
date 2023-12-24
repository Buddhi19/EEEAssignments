def expression_g1(x):
    return ((10 - x**3) / 4) ** 0.5


def expression_g2(x):
    return (10 / (4 + x)) ** 0.5


def shape(x):
    return format(x, "1.6f")


def newton_raphson(x):
    return x - (x**3 + 4 * x**2 - 10) / (3 * x**2 + 8 * x)


def fixed_point():
    global_count = 1
    g1_x = 1.5
    g2_x = 1.5

    while global_count < 4:
        t1 = g1_x
        g1_x = expression_g1(t1)
        tolerance1 = abs(t1 - g1_x)

        t2 = g2_x
        g2_x = expression_g2(t2)
        tolerance2 = abs(t2 - g2_x)

        print(
            f"{global_count}&{shape(g1_x)}&{shape(tolerance1)}&{shape(g2_x)}&{shape(tolerance2)}"
        )
        global_count += 1


global_count = 1
x = 1.5

while global_count < 4:
    t = x
    x = newton_raphson(t)
    tolerance = abs(x - t)

    print(f"{global_count}&{shape(x)}&{shape(tolerance)}")
    global_count += 1
