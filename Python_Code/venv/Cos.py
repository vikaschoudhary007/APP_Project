# Using Taylor series expansion to calculate the Cosine function
# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...

# x is the angle in degrees
# n is the number of terms in Taylor series
def cos(x):
    n = 100

    result = 1.0
    sign = -1.0
    power = x * x
    fact = 2.0

    for i in range(1, n):
        result += sign * power / fact
        sign *= -1.0
        power *= x * x
        fact *= (2 * i + 1) * (2 * i + 2)
        #print("fact is:" ,fact)

    return result
