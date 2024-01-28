import numpy as np

epsilon = 8.859 * 10 ** (-12)
sigma = 0.36


class solution:
    def __init__(self, a, N, k):
        self.a = a
        self.N = N
        self.k = k
        self.r = self.k / 10
        self.b = self.r
        self.h = (self.b - self.a) / self.N

    def f(self, x):
        return (sigma) * (np.exp(x) * x**2) / (epsilon * self.r**2)

    def evaluate(self):
        answer = 0
        for i in range(self.N + 1):
            if i == 0 or i == self.N:
                answer += 2 * self.h * self.f(self.a + i / self.N)

            else:
                answer += self.h * self.f(self.a + i / self.N)

        return answer

    def second_derivative(self, x):
        return (x**2 + 4 * x + 2) * np.exp(x)

    def error(self):
        error = -1 * (self.b - self.a) * self.h**2 / 12
        error *= self.second_derivative(self.b)
        return error


if __name__ == "__main__":
    for k in range(1, 11):
        print(f"For k={k}")
        N = 10 ** (6)
        sol = solution(0, N, k)
        print(f"Solution is {sol.evaluate()}")
        print(f"Error is {sol.error()}")
        print()
