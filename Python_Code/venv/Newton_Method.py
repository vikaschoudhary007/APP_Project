# In this implementation, newton_method is a function that takes as input the function f, its derivative df,
# an initial guess x0, an error tolerance eps, and a maximum number of iterations max_iter. It uses the Newton method
# to solve for the root of the function f, starting at x0 and iteratively updating the guess using the formula x - f(
# x)/f'(x). The function stops iterating when the absolute value of f(x) is less than eps, or when the derivative f'(
# x) is zero. It returns the solution x, or None if no solution was found within the maximum number of iterations. In
# this case, the function f is defined as x - sin(x) - pi/2, and its derivative df is defined as 1 - cos(x). The
# initial guess x0 is set to pi/2, since we know that the root is close to this value. The resulting alpha value is
# printed to the console.
from Python_Code.venv.Cos import cos
from Python_Code.venv.PI import PI
from Python_Code.venv.Sin import sin


def newton_method(x0, eps=1e-6, max_iter=1000):
    x = x0
    for i in range(max_iter):
        if df(x) == 0:
            raise ValueError("Error: derivative is zero")
        x0 = x - (f(x) / df(x))
        if abs(x0 - x) < eps:
            return x0
        x = x0
    return x0


def f(x):
    return x - sin(x) - (PI() / 2)


def df(x):
    return 1 - cos(x)


def shift_distance(x0, R):
    try:
        alpha = newton_method(x0)
        l = 2 * R * (1 - cos(alpha / 2))
        return l / 2
    except ValueError as e:
        print(e)
        return None
