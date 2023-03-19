# Using Taylor series expansion to calculate the sign function
# sin(x) = x - (x^3)/3! + (x^5)/5! - (x^7)/7! + ...

# x is the angle in degrees
# n is the number of terms in Taylor series


def sin(x):
    """
    Calculate the sine of an angle in radians using Taylor series expansion.

    Args:
    x (int or float): The angle in radians.

    Returns:
    The sine of the given angle.

    Raises:
    TypeError: If the input is not an int or float.

    Note:
    Uses the Taylor series expansion formula for sine:
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")

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
