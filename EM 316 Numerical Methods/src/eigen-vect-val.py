import numpy as np
from sympy import *  # type:ignore

A = Matrix([[-2, 1, 4], [1, 1, 1], [4, 1, -2]])

print(A.eigenvals())
print(A.eigenvects())
