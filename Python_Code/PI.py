# Using Leibniz Formula to calculate approximate value of PI,
# Leibniz formula for PI, is an infinite series that can be used to approximate the value of pi.
# π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
# this formula uses alternating signs to converge to PI.

# Following is the python code implementation of Leibniz Formula

# number of terms used for approximation

def PI():

    number_of_terms = 1000000

    sum = 0
    sign = 1;

    for i in range(number_of_terms):

        new_term = sign/(2*i + 1)
        sum = sum+new_term
        sign *= -1;

    # use this sum to estimate PI

    PI = 4 * sum;
    return PI

