def expression_x1(x2, x3):
    return (-1 + 2 * x2 - 3 * x3) / 5


def expression_x2(x1, x3):
    return (2 + 3 * x1 - 1 * x3) / 9


def expression_x3(x1, x2):
    return (3 - 2 * x1 + x2) / (-7)


def round(num):
    return format(num, ".3f")


X1, X2, X3 = 0, 0, 0

T1, T2, T3 = float("inf"), float("inf"), float("inf")

k = 1
while True:
    if round(X1) == round(T1) and round(X2) == round(T2) and round(X3) == round(T3):
        break
    T1, T2, T3 = X1, X2, X3

    X1 = expression_x1(T2, T3)
    X2 = expression_x2(T1, T3)
    X3 = expression_x3(T1, T2)

    print(
        f"{k}&{round(X1)}&{round(X1-T1)}&{round(X2)}&{round(X2-T2)}&{round(X3)}&{round(X3-T3)}\\\\"
    )
    k += 1
