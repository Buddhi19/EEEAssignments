def expression(x):
    return (10 - 4 * x**2) ** (1 / 3)

def expression_2(x):
    return ((10-x**3)/4)**(0.5)

global_count = 0


def iteration(lower, upper):
    global global_count
    global_count += 1
    x = (lower + upper) / 2
    x_assumed = expression(x)
    error = x_assumed - x
    print(f"{global_count}&{format(x,"1.6f")}&{format(x_assumed,"1.6f")}&{format(error,"1.6f")}")
    if abs(error) < 10 ** (-5):
        return
    if error > 0:
        lower = x
        return iteration(lower, upper)
    else:
        upper = x
        return iteration(lower, upper)


iteration(1, 2)
