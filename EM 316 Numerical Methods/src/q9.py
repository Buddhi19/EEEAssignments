import numpy as np


def expression(r):
    return 0.01 - np.exp(-0.005 * r) * np.cos(0.05 * (2000 - 0.01 * r**2) ** 0.5)


def derivative(r):
    f1 = 0.005 * np.exp(-0.005 * r) * np.cos(0.05 * (2000 - 0.01 * r**2) ** 0.5)
    f2 = (
        np.exp(-0.005 * r)
        * np.sin(0.05 * (2000 - 0.01 * r**2) ** 0.5)
        * 0.001
        * r
        / (2000 - 0.01 * r**2) ** 0.5
    )
    return f1 - f2


def shape(x):
    return format(x, "1.6f")


global_count = 0


def bisect_method(lower, upper):
    global global_count
    global_count += 1
    r = (lower + upper) / 2
    f_r = expression(r)
    print(f"{global_count}&{shape(r)}&{shape(f_r)}")
    if global_count >= 4:
        return
    if f_r > 0:
        lower = r
        return bisect_method(lower, upper)
    else:
        upper = r
        return bisect_method(lower, upper)


def newtons_raphson():
    R_0 = 400
    R = R_0
    count = 1
    while count < 5:
        f_r = expression(R)
        R = R - f_r / derivative(R)
        print(f"{count}&{shape(R)}&{shape(f_r)}")
        count += 1


if __name__ == "__main__":
    newtons_raphson()
