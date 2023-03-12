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
