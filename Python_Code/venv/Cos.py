# Using Taylor series expansion to calculate the Cosine function
# cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...
# x is the angle in degrees
# n is the number of terms in Taylor series


def cos(x):
    """
    This function approximates the cosine of an angle in degrees using Taylor series expansion.

    Args:
        x (float): The angle in degrees to calculate the cosine for.

    Returns:
        float: The approximation of the cosine of the given angle.

    Raises:
        TypeError: If the input argument `x` is not a number.

    Note:
        This function uses 100 terms in the Taylor series expansion to calculate the cosine.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")

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

    return result
