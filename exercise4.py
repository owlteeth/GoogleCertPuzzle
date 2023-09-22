# eek, this was the hardest so far (and harder than number 5)
# three operations increment, decrement, divide by 2 if even
# find shortest sequence to reduce n<= 309 digits (why?) to 1
# ok, so I know how to write a working recursive solution,
# but it doesn't pass a bunch of their tests with large values
# memoizing passed one more test so I guess it's about recursion depth not speed
# I'm not allowed to up the recursion limit to what's needed
# In the end I needed to lean on StackOverflow to understand how to write the iterative version
# in future problems like this, remember to look at the patterns in the least significant bits
# Completed in: 7 hrs, 34 mins, 7 secs..

import math

memo = {}


def solution(n):
    """Implements the function specced in (forgotten the name) (fourth challenge on https://foobar.withgoogle.com/)
    Returns a string representation of the number of fuel pellet division steps required.
    """
    n = int(n)
    # steps = solution_recursive(n)
    steps = solution_iterative(n)
    return steps


def solution_recursive(n):
    if n == 1:
        return 0

    if n % 2:
        m = n - 1
        o = n + 1
        if m not in memo:
            memo[m] = solution_recursive(m)
        if (o) not in memo:
            memo[o] = solution_recursive(o)
        return 1 + min(memo[m], memo[o])

    else:
        h = n // 2
        if h not in memo:
            memo[h] = solution_recursive(h)
        return 1 + memo[h]


def solution_iterative(n):
    steps = 0
    while n > 1:
        if not n % 2:
            n = n / 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1
        steps += 1
    return steps


# didn't need
def nearest_power_of_2(n):
    l = math.log(n, 2)
    lf = math.floor(l)
    lc = math.ceil(l)
    a = l - lf
    b = lc - l
    if min(a, b) == a:
        return 2**lf
    else:
        return 2**lc
