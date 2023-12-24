def expression_x1(x2, x3):
    return (8 - 2 * x2 - x3) / 5


def expression_x2(x1, x3):
    return (20 - 4 * x1 - 15 * x3) / 11


def expression_x3(x1, x2):
    return (31 - 7 * x1 - 8 * x2) / 16


def round(num):
    return format(num, ".4f")


X1, X2, X3 = 0.5, 0.5, 0.5
for k in range(1, 3):
    T1, T2, T3 = X1, X2, X3
    X1 = expression_x1(T2, T3)
    X2 = expression_x2(X1, T3)
    X3 = expression_x3(X1, X2)

    print(
        f"{k}&{round(X1)}&{round(X1-T1)}&{round(X2)}&{round(X2-T2)}&{round(X3)}&{round(X3-T3)}\\\\"
    )
