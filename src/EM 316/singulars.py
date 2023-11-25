import numpy as np
from sympy import *  # type ignore

mat = Matrix([[0.780, 0.563], [0.913, 0.659]])

print(latex(mat * mat.T))


def my_calculation(mat):
    mat = mat * mat.T
    l = symbols("\\lambda")
    check_mat = mat - l * Matrix([[1, 0], [0, 1]])

    determinant = check_mat.det()
    print(determinant)

    print(solve(determinant, l, dict=True))

    ans = solve(determinant, l)
    print(ans)

    for i in range(len(ans)):
        print(f"\\sigma_{i+1}&={ans[i]**0.5}")


def built_in(mat):
    u, s, v = mat.singular_value_decomposition()
    print(s)


if __name__ == "__main__":
    my_calculation(mat)
