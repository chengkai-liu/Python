"""
Highly divisible triangular numbers
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""
from __future__ import print_function
from math import sqrt

try:
    xrange  # Python 2
except NameError:
    xrange = range  # Python 3


def count_divisors(n):
    nDivisors = 0
    for i in xrange(1, int(sqrt(n)) + 1):
        if n % i == 0:
            nDivisors += 2
    # check if n is perfect square
    if n ** 0.5 == int(n ** 0.5):
        nDivisors -= 1
    return nDivisors


def solution():
    """Returns the value of the first triangle number to have over five hundred
    divisors.
    
    >>> solution()
    76576500
    """
    tNum = 1
    i = 1

    while True:
        i += 1
        tNum += i

        if count_divisors(tNum) > 500:
            break

    return tNum


if __name__ == "__main__":
    print(solution())
