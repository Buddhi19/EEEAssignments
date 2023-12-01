import numpy as np
import matplotlib.pyplot as plt


def plot_graphs():
    X = np.arange(-1, 4, 0.1)
    Y1 = np.sin(X)
    Y2 = (X / 2) ** 2
    plt.plot(X, Y1, X, Y2)
    plt.title("Figure 1")
    plt.show()


def function(x):
    return (x / 2) ** 2 - np.sin(x)


def shape(num):
    return format(num, ".4f")


iterations = 0


def bisect_method(L, U):
    global iterations
    iterations += 1
    if iterations >= 10:
        return
    x = (L + U) / 2
    result = function(x)
    print(f"x={shape(x)} f(x)={shape(result)}")
    if result > 0:
        return bisect_method(L, x)
    else:
        return bisect_method(x, U)


bisect_method(1, 2)
plot_graphs()
