import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

RESULTS = dict()

EPSILON = 4 * 10 ** (-9) / (36 * np.pi)
P_0 = 10 ** (-10)

ITERATIONS = 10000


def evaluate(v1, v2, z, h):
    return (v1 + v2) / 2 + (z * P_0 * h**2) / (10 * EPSILON)


def analytical(z):
    return -3 * np.pi * z**3 / 100 + (10 + 3 * np.pi) * z


class bisect_method:
    def __init__(self) -> None:
        self.initial_conditions()

    def initial_conditions(self):
        RESULTS[0] = 0
        RESULTS[10] = 100

    def initial_guess(self, L, U):
        z = (L + U) / 2
        h = (U - L) / 2
        if h < 0.01:
            return
        v1, v2 = RESULTS[L], RESULTS[U]
        RESULTS[z] = evaluate(v1, v2, z, h)
        self.initial_guess(z, U)
        self.initial_guess(L, z)
        return


class iterative_method:
    def __init__(self) -> None:
        self.without_guess()

    def without_guess(self):
        RESULTS[0] = 0
        i = 1
        while i < 100:
            RESULTS[i] = 0.1
            i += 1
        RESULTS[100] = 100

    def iteration_without_guess(self):
        i = 99
        temp = RESULTS
        while i > 0:
            temp[i] = evaluate(RESULTS[i - 1], RESULTS[i + 1], i / 10, 0.1)
            i -= 1

        for key in RESULTS:
            RESULTS[key] = temp[key]


class Demonstration:
    def __init__(self):
        self.fig = plt.figure()
        self.temp = self.fig.add_subplot(1, 1, 1)

    def animate(self, i):
        if i > len(RESULTS):
            plt.close()
            return
        X = list(RESULTS.keys())[:i]
        Y = list(RESULTS.values())[:i]

        X2 = list(sorted(RESULTS.keys()))
        Y2 = [analytical(x) for x in X2]

        self.temp.clear()
        self.temp.plot(X2, Y2, c="black")
        plt.title("Bisect Method Animation")
        self.temp.scatter(X, Y, linewidths=0.001)
        self.temp.scatter(X[-2:], Y[-2:], c="r", linewidths=0.001)

    def animate_2(self, i):
        if i > len(RESULTS):
            plt.close()
            return
        X = list(RESULTS.keys())[:i]
        Y = list(RESULTS.values())[:i]

        X2 = list(sorted(RESULTS.keys()))
        Y2 = [analytical(x / 10) for x in X2]

        self.temp.clear()
        plt.title("Iterative Method Animation (Skipped)")
        self.temp.plot(X2, Y2, c="black")
        self.temp.plot(X, Y)

    def show_animation(self, flag):
        fn = self.animate
        interval = 30
        if flag:
            fn = self.animate_2
            interval = 5
        self.animation_ = animation.FuncAnimation(
            self.fig, fn, interval=interval, repeat=False, cache_frame_data=False  # type: ignore
        )
        plt.show()


def main_bisect():
    method = bisect_method()
    method.initial_guess(0, 10)
    Demo = Demonstration()
    Demo.show_animation(flag=False)
    RESULTS.clear()


def main_iterative_method():
    method = iterative_method()
    for iter in range(ITERATIONS):
        method.iteration_without_guess()
        if iter % 800 == 0 and iter // 800 < 8:
            Demo = Demonstration()
            Demo.show_animation(flag=True)


if __name__ == "__main__":
    main_bisect()
    main_iterative_method()
