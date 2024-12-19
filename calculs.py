import numpy
import math

def f(x):
    return x**2 - 8 * numpy.log(x)
x = numpy.array([1, 2, 3, 4, 5])
y = f(x)
y = [f(1), f(2), f(3), f(4), f(5)]
print(y)

def f(x):
    return x**2 - 8 * math.log(x)
x = 5
y = f(x)
print(y)

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

if__name__ == '__main__':
    x = numpy.array([1, 2, 3, 4, 5])
    y = f(x)
    middle = solve_equation(f, left=1, right=2)
    print(middle)
    print(f(middle)

