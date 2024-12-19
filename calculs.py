import numpy
import matplotlib.pyplot as plt
import math


def f(x):
    return x**2 - 8 *numpy.log(x)


left = 1
right = 2
précision = 10**-5


def solve_equation(f, left, right, précision=10**-5):
    while right - left >= précision:
        middle = (left + right) / 2

        if f(middle) == 0:
            return middle
        elif f(middle) * f(left) < 0:
            right = middle
        elif f(middle) * f(right) < 0:
            left = middle
    return middle

if __name__ == '__main__':
    x = numpy.array([1, 2, 3, 4, 5])
    y = f(x)
    middle = solve_equation(f, left=1, right=2)
    print(middle)
    print(f(middle))

def plot_function(f, start, end, step=0.01):
    x = numpy.arange(start, end, step)
    print(x) # pour voir les valeurs de x
    y = f(x)
    print(y) # pour voir les valeurs de y
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    plot_function(f, 1, 5)
    plot_function(f, 1, 5, 0.1)
