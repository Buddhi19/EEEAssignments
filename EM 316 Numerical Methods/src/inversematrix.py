from sympy import *  # type ignore

init_printing()
c, r1, r2, l1, l2, s, rc = symbols("C R_1 R_2 L_1 L_2 s R_c")

mat = Matrix(
    [
        [s + r1 / l1, 0, 1 / l1],
        [0, s + r2 / l2, -1 / l2],
        [-1 / c, 1 / c, s + 1 / (c * rc)],
    ]
)


def print_inverse():
    print(latex(simplify(mat.inv() * mat.det())))


def print_determinant():
    print(latex(simplify(1 / (mat.det() * (c * l1 * l2 * rc) ** 2))))


D = Matrix([[0, 0, 1]])

P = mat.inv()

v1, v2 = symbols("V_1(s) V_2(s)")

X = Matrix([[v1 / l1], [v2 / l2], [0]])

ans = D * P * X

print(latex(ans))
