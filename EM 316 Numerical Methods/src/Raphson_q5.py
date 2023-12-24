def next_term(x):
    return (2 * x**3 - 0.165 * x**2 + 3.993 * 10 ** (-4)) / (3 * x**2 - 0.33 * x)

Found_Root=0.1776521994207141

x_0 = 0.2
count = 0
x = x_0
while count < 3:
    count += 1
    x = next_term(x)
    # print(f"x = {x}")
    print(f"{count}&{format(x,"1.10f")}&{format(x-Found_Root,"1.10f")}")
