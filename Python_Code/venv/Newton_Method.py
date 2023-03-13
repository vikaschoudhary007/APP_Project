# In this implementation, newton_method is a function that takes as input the function f, its derivative df,
# an initial guess x0, an error tolerance eps, and a maximum number of iterations max_iter. It uses the Newton method
# to solve for the root of the function f, starting at x0 and iteratively updating the guess using the formula x - f(
# x)/f'(x). The function stops iterating when the absolute value of f(x) is less than eps, or when the derivative f'(
# x) is zero. It returns the solution x, or None if no solution was found within the maximum number of iterations. In
# this case, the function f is defined as x - sin(x) - pi/2, and its derivative df is defined as 1 - cos(x). The
# initial guess x0 is set to pi/2, since we know that the root is close to this value. The resulting alpha value is
# printed to the console.


from PI import PI
from Sin import sin
from Cos import cos

def newton_method(f, df, x0, eps=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < eps:
            return x
        dfx = df(x)
        if dfx == 0:
            break
        x -= fx / dfx
    return None


def f(x):
    return x - sin(x) - PI() / 2


def df(x):
    return 1 - cos(x)

R = 0.5
print("HEll0")

alpha = newton_method(f, df, PI() / 2)
l = 2 * R * (1 - cos(alpha / 2))
print("alpha:", alpha)
print("l:", l)
