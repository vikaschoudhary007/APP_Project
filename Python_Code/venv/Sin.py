# Using Taylor series expansion to calculate the sign function
# sin(x) = x - (x^3)/3! + (x^5)/5! - (x^7)/7! + ...

# x is the angle in degrees
# n is the number of terms in Taylor series


def sin(x):
    n = 100

    result = 0.0
    sign = 1.0
    power = x
    fact = 1.0

    for i in range(n):
        result += sign * power / fact
        sign *= -1.0
        power *= x * x
        fact *= (2 * i + 2) * (2 * i + 3)

    return result
