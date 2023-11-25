CORRECT_VALUE = 10 ** (1 / 2)


def next_term(x):
    return (x + 10 / x) / 2


x = 3.0
count = 0
error = abs(CORRECT_VALUE - x)
while error > 10 ** (-8):
    count += 1
    error = abs(CORRECT_VALUE - x)
    print(f"{count}&{format(x,"1.10f")}&{format(error,"1.12f")}")
    x = next_term(x)
