import numpy as np
import sympy as sp


x = sp.symbols("x")


def polynomial(poly_x, poly_y):
    mat = []
    poly = poly_y[0]

    mat.append(poly_y)
    order = 1
    while True:
        if len(mat[-1]) == 1:
            break
        order_coefficients = []
        for i in range(len(mat[-1]) - 1):
            f = (mat[-1][i + 1] - mat[-1][i]) / (poly_x[i + order] - poly_x[i])
            order_coefficients.append(f)

        mat.append(order_coefficients)
        order += 1
    # print(mat)
    for i in range(1, len(mat)):
        term = mat[i][0]
        for j in range(i):
            term *= x - poly_x[j]

        poly += term

    return poly


def point_value(poly, n):
    return poly.subs(x, n)


if __name__ == "__main__":
    poly_x = [0.2, 0.4, 0.6, 0.8, 1.0]
    poly_y = [2.40, 3.00, 2.55, 2.24, 1.72]
    poly = polynomial(poly_x, poly_y)
    print(poly)
    print(point_value(poly, 0.75))
