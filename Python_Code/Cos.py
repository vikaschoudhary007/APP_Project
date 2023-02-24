# Using Taylor series expansion to calculate the Cosine function
# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...

# x is the angle in degrees
# n is the number of terms in Taylor series

import PI;

def cos(degrees):

    n = 1000

    x = (PI.PI() / 180) * degrees;

    result = 1.0
    sign = -1.0
    power = x * x
    fact = 2.0

    for i in range(1, n):
        result += sign * power / fact
        sign *= -1.0
        power *= x * x
        fact *= (2 * i) * (2*i + 1)

    return  result

print("Cos(x) value is", cos(45))