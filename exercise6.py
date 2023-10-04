"""
Implementation of code to generate the answers needed by exercise 6 on foobar.withgoogle.com 
(The Grandest Staircase of Them All). Actual solution code submitted was just the lookup table
produced (see comment section below).

I spent about a day total noodling at the question from first principles - some records of thought
processes at end of file. After googling around "how to break up a number by summation" I realised 
that the problem corresponded to the idea of 'distinct partitions of an integer', and that I wasn't
math-competent enough to reinvent an algorithm for it. Therefore I found an implementation on OEIS 
(credited below) and used it to generate the answers.
"""

from functools import lru_cache
from math import isqrt

# the-grandest-staircase-of-them-all

@lru_cache(maxsize=None)
"""Function by Chai Wah Wu, Sep 08 2021. Source: https://oeis.org/A000009"""
def A000009(n):
    return (
        1
        if n == 0
        else A010815(n)
        + 2 * sum((-1) ** (k + 1) * A000009(n - k**2) for k in range(1, isqrt(n) + 1))
    )

def A010815(n):
"""Function by Chai Wah Wu, Sep 08 2021. Source: https://oeis.org/A010815"""
    m = isqrt(24 * n + 1)
    return (
        0
        if m**2 != 24 * n + 1
        else ((-1) ** ((m - 1) // 6) if m % 6 == 1 else (-1) ** ((m + 1) // 6))
    )  # Chai Wah Wu, Sep 08 2021

def staircases(n):
    """Calls the OEIS function above with n, then subtracts 1 from the response. This
    is necessary to remove the single partition of size 1, because that doesn't count
    as a 'staircase' for the exercise. """
    return A000009(n) - 1

def make_lut():
  return {n: staircases(n) for n in range(201)}

print(make_lut())

""" 
Code above generates a lookup table for n<=200. Rather than do the additional work to convert
the memoization decorator into a memoized version of the OEIS functions that would run in Python 2
for foobar.withgoogle, I just submitted the lookup table as the solution: code follows.

lut = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 7, 10: 9, 11: 11, 12: 14, 13: 17, 14: 21, 15: 26, 16: 31, 17: 37, 18: 45, 19: 53, 20: 63, 21: 75, 22: 88, 23: 103, 24: 121, 25: 141, 26: 164, 27: 191, 28: 221, 29: 255, 30: 295, 31: 339, 32: 389, 33: 447, 34: 511, 35: 584, 36: 667, 37: 759, 38: 863, 39: 981, 40: 1112, 41: 1259, 42: 1425, 43: 1609, 44: 1815, 45: 2047, 46: 2303, 47: 2589, 48: 2909, 49: 3263, 50: 3657, 51: 4096, 52: 4581, 53: 5119, 54: 5717, 55: 6377, 56: 7107, 57: 7916, 58: 8807, 59: 9791, 60: 10879, 61: 12075, 62: 13393, 63: 14847, 64: 16443, 65: 18199, 66: 20131, 67: 22249, 68: 24575, 69: 27129, 70: 29926, 71: 32991, 72: 36351, 73: 40025, 74: 44045, 75: 48445, 76: 53249, 77: 58498, 78: 64233, 79: 70487, 80: 77311, 81: 84755, 82: 92863, 83: 101697, 84: 111321, 85: 121791, 86: 133183, 87: 145577, 88: 159045, 89: 173681, 90: 189585, 91: 206847, 92: 225584, 93: 245919, 94: 267967, 95: 291873, 96: 317787, 97: 345855, 98: 376255, 99: 409173, 100: 444792, 101: 483329, 102: 525015, 103: 570077, 104: 618783, 105: 671417, 106: 728259, 107: 789639, 108: 855905, 109: 927405, 110: 1004543, 111: 1087743, 112: 1177437, 113: 1274117, 114: 1378303, 115: 1490527, 116: 1611387, 117: 1741520, 118: 1881577, 119: 2032289, 120: 2194431, 121: 2368799, 122: 2556283, 123: 2757825, 124: 2974399, 125: 3207085, 126: 3457026, 127: 3725409, 128: 4013543, 129: 4322815, 130: 4654669, 131: 5010687, 132: 5392549, 133: 5802007, 134: 6240973, 135: 6711479, 136: 7215643, 137: 7755775, 138: 8334325, 139: 8953855, 140: 9617149, 141: 10327155, 142: 11086967, 143: 11899933, 144: 12769601, 145: 13699698, 146: 14694243, 147: 15757501, 148: 16893951, 149: 18108417, 150: 19406015, 151: 20792119, 152: 22272511, 153: 23853317, 154: 25540981, 155: 27342420, 156: 29264959, 157: 31316313, 158: 33504745, 159: 35839007, 160: 38328319, 161: 40982539, 162: 43812109, 163: 46828031, 164: 50042055, 165: 53466623, 166: 57114843, 167: 61000703, 168: 65139007, 169: 69545357, 170: 74236383, 171: 79229675, 172: 84543781, 173: 90198445, 174: 96214549, 175: 102614113, 176: 109420548, 177: 116658615, 178: 124354421, 179: 132535701, 180: 141231779, 181: 150473567, 182: 160293887, 183: 170727423, 184: 181810743, 185: 193582641, 186: 206084095, 187: 219358314, 188: 233451097, 189: 248410815, 190: 264288461, 191: 281138047, 192: 299016607, 193: 317984255, 194: 338104629, 195: 359444903, 196: 382075867, 197: 406072421, 198: 431513601, 199: 458482687, 200: 487067745}

def solution(n):
  return lut[n]
"""

"""
RECORD OF THINKING

ADDED AT TOP: 
    After some thinking about how to generate the sets, I notice that the code that 
    I actually submit for the exercise does not have to be the same as the generating code: it just 
    has to be a lookup table of 196 precalcuated values! Noticing this may be part of the challenge.
    Maybe I don't even have to generate them if they are already on that one website with all the 
    number series? I'll keep thinking about how to do it elegantly though.
This is about finding an decomposition of an integer, like factoring but additive, don't know what the word for that is
Some googling suggests that what I want is "partitions"
This isn't quite as simple as finding the partitions of a number because repeats
are not allowed. 
(added: https://en.wikipedia.org/wiki/Composition_(combinatorics) suggests that what we are after 
are "distinct partitions")
Trying to think more about the problem before I look at other people's code:
- (n-1, 1) is always a solution
- given column a and b, always ok to move up to ceil(a/2)
- maybe the longest solution could be found by starting with 1, adding 1 each time until the sum 
overshoots n, and then subtracting which ever step was equal to the difference
- but I don't see a way to churn through permutations from that point
- what happens if I do a managable one by hand? say 11
11
 10,1
 9,2
 8,3
  8,2,1
 7,4
  7,3,1
 6,5
  6,4,1
   6,3,2
  5,4,2
(UPDATE derp i missed a bunch, need to isolate the missed process)
so a tree is formed, but what rule is being followed here?
What if we did:
- start a stack with [[n]]
- take list off stack, for each number in turn, check if moving 1 rightwards is "legal"
- if so, add that new list to the stack
- once all numbers have been checked, remove that list into a "finished" set
- when stack empty, count solutions in bin
that seems like it would work, however, can we avoid repeatedly rediscovering that a
list ending [...6,4,1] can be tranformed into [...6,3,2]? So we want to save whole subtrees.
So actually, we need to do this in reverse, like, if we find the solutions for 10:
9,1
8,2
7,3
 7,2,1
6,4
 6,3,1
 then we can make the solutions for 11 from them by adding 1 to the last number in all of them unless illegal, then the second, and so on:
9,2
8,3
7,4
6,5
10,1
9,2
8,3
 7,3,1
7,4
 6,4,1
8,2,1
7,3,1

no, doesn't give 6,3,2; 5,4,2; 5,3,2,1 how would that have been generated?, 
how did I miss originally when working out 11?
how did I miss 5,4,1 when working out 10?

process: test adding 1 to each column biggest -> smallest, 
fail if adding 1 to a column makes it equal to the next biggest
if smallest column is not 1, add new column of 1
6,1 -> [7,1 6,2]
5,2 -> [6,2 5,3, 5,2,1]
4,3 -> [5,3, !(4,4) 4,3,1] 
4,2,1 -> [5,2,1 4,3,1 !(4,2,2)]

yes, that works, but wastes time recalculating several, how can that be avoided?
if we just add to each but the last digit:
6.1 -> 7.1
5.2 -> 6.2
4.3 -> 5.3
4.2.1 -> 5.2.1, 4.3.1
that works, but maybe by a fluke - not sure how it is that new columns never made?
lets go back to start

2.1 -> 3.1
3.1 -> 4.1 ... yeah how do we get to 3.2?
new rules:
take each input(x,y...z), add (x+1,y...z), (x,y+1...z) to output whereever legal
    and if input z>1, add to output (x,y,z,1)
    and if input z-1,z = 4,1 also add as 3,2

2.1 -> 3.1

3.1 -> 4.1, 3.2

4.1 -> 4.2
3.2 -> 4.2, 3.2.1

inkling that there's some way to make this neater by keeping even and odd outputs in seperate bins?

no this whole approach is missing something. There's a thing where you need to check for each column whether 
one has become equal to twice-plus-one of the next smallest, because then you can break it into two new columns
Thinking about this as a staircase is introducing artificial complexity, it needs to be thought about as just
all ways of breaking up the number, using some other way of iterating. I need to look at wikipedia spoilers 
at this point and determine if there's any way on earth I'd come up with the canonical solution
"""