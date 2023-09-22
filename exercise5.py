def solution(M, F):
    """
    Implements the function specced in bomb-baby (fifth challenge on https://foobar.withgoogle.com/)
    Returns a string representation of the number of replication steps required.
    Completed in 22 hrs, 16 mins, 35 secs (but about 3 hours actually, as I left it overnight)
    Took more notes on thought process this time, see end of file
    """
    m, f = int(M), int(F)
    if impossible(m, f):
        return "impossible"
    else:
        steps = solve_better(m, f)
        return str(steps)


# test 4 of 5 requires the outcome of impossible
def impossible(m, f):
    # always impossible if either < 1
    if m < 1 or f < 1:
        return True
    # always possible if either == 1
    if m == 1 or f == 1:
        return False
    # impossible if both numbers are even
    if m % 2 == 0 and f % 2 == 0:
        return True
    # impossible if one evenly divides another
    if m % f == 0 or f % m == 0:
        return True
    # otherwise presumed possible
    return False


def solve_naive(m, f):
    steps = 0
    # first reduce down to 1 on one side
    # could be better if I knew that the smaller/larger number will always reach 1 firdt
    # but I don't know that rn
    while (m > 1) and (f > 1):
        if m < f:
            f = f - m
        else:
            m = m - f
        steps += 1
    # does adding this bit pass test 4?
    if (m < 1) or (f < 1):
        return "impossible"
    # yes it does, meaning that I miss an impossibility case up front, but that might not matter
    # then shortcut the rest of the steps
    remaining = max(m, f) - 1
    return steps + remaining


def solve_better(m, f):
    steps = 0
    # reduction by division
    while (m > 1) and (f > 1):
        if m < f:
            factor = f // m
            steps += factor
            f = f - (m * factor)
        else:
            factor = m // f
            steps += factor
            m = m - (f * factor)
    # check for the impossibility case I missed
    if (m < 1) or (f < 1):
        return "impossible"
    # then shortcut the rest of the steps
    remaining = max(m, f) - 1
    return steps + remaining


assert solution(1, 1) == "0"
assert solution(99, 0) == "impossible"
assert solution(10, 10) == "impossible"
assert solution(2, 1) == "1"
assert solution(4, 7) == "4"

""" THOUGHTS
you have 1 M and 1 F
you are provided with target M and F
each iteration step can either a) increment F by M or b) increment M by F.
Thoughts:
- might be better to start with the targets and reversed rules, and see if you can reach (1,1)
    so rule a) dec F by M, rule b) dec M by F
- a greedy attempt might be:
    see if M % F is 1, in which case M can be reduced to 1 by repeating rule b, then F can be reduced to 1 by
    repeating rule a
or vice versa, so in fact the solution is symmetric, (x,y) takes same steps as (y,x)
so it's definitely possible at any point if either F==M==1 (no steps) or (F%M OR M%F)==1
is there any other case where it's possible?
yes, because (4,7) is possible in four steps - why?
4,7
4,3
1,3
1,2
1,1
that means that (4,11) and (11,7) are both also posible
we also want to always be subtracting the smaller number from the bigger number
    and that means that we must never get to numbers identical (except 1,1) or one double the other (except 2,1)
    that is, if either mod is 0 it's impossible
    in fact is it impossible if both numbers are even? I think so, because subtracting even from even always makes even
 the verification process takes forever with this one, are they assuming there is search going on?
so my naive code passes tests 1, 2 and 5, but fails 3 (so it's taking too long to work, need to accelerate the first part)
and fails 4 (So I'm missing an impossibility criterion)
4 seems to be caused by values ending up smaller than 1. Not sure why, but fortunately I can just test for that halfway 
through the solution process and return a sneaky "impossible", and that's good enough.
I can speed things up just by doing a division and subtraction 
"""
