# division problem
# three operations increment, decrement, divide by 2 if even
# find shortest sequence to reduce n<= 309 digits (why?) to 1
# ok, so I know how to write  a wokrign recursive solution,
# but  it doesn't pass a  bunch of their tests
# memoizing got one more test
# I'm not allowed to up the recursion limit to what's needed
# need to rewrite as iterative I guuess
# I needed to lean on https://stackoverflow.com/questions/39588554/minimum-number-of-steps-to-reduce-number-to-1/39589499#39589499
# Completed in: 7 hrs, 34 mins, 7 secs..

import math

memo = {}


def solution_recursive(n):
    if n == 1:  # base case
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


def approximate_steps_remaining(n):
    return math.ceil(math.log(n, 2) * 2)


"""
def tester():
    ns = range(1, 310)
    spreads = range(0, 11)
    results = []
    for spread in spreads:
        line = [solution_recursive(n, spread, 0) for n in ns]
        print(f"total steps using spread {spread}: {sum(line)}")
"""


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


def solution(n):
    n = int(n)
    # steps = solution_recursive(n)
    steps = solution_iterative(n)
    return steps


print(solution(4))
print(solution(15))
print(solution(301))
print(solution(10**300))
# tester()

"""
If I use -1 at point a, tests  1,2,4 and 9 pass
If I use +1 instead, test 8 passes and 4 fails!
"""
