import numpy as np
import sympy as sp

x = sp.symbols("x")


def polynomial(poly_x, poly_y):
    poly = 0
    for i in range(len(poly_x)):
        numerator = 1
        denominator = 1
        for j in range(len(poly_x)):
            if i == j:
                continue
            numerator *= x - poly_x[j]
            denominator *= poly_x[i] - poly_x[j]

        poly += numerator * poly_y[i] / denominator

    return poly


def point_value(poly, n):
    val = poly.subs(x, n)
    return val


if __name__ == "__main__":
    poly_x = [0, 1, 2, 5.5, 11]
    poly_y = [0.5, 3.134, 5.3, 9.9, 10.2]
    poly = polynomial(poly_x, poly_y)
    print(poly)
    print(point_value(poly, 8))
