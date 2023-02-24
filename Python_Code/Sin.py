# Using Taylor series expansion to calculate the sign function
# sin(x) = x - (x^3)/3! + (x^5)/5! - (x^7)/7! + ...

# x is the angle in degrees
# n is the number of terms in Taylor series

import PI;

def sin(degrees):

    n = 1000

    x = (PI.PI() / 180) * degrees;

    result = 0.0
    sign = 1.0
    power = x
    fact = 1.0

    for i in range(n):
        result += sign * power / fact
        sign *= -1.0
        power *= x * x
        fact *= (2*i + 2) * (2*i + 3)

    return  result

print("Sin(x) value is", sin(30))