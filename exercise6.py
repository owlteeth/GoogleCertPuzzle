"""
THOUGHTS
ADDED AT TOP: 
    After some thinking about how to generate the sets, I notice that the code that 
    I actually submit for the exercise does not have to be the same as the generating code: it just 
    has to be a lookup table of 196 precalcuated values! Noticing this may be part of the challenge.
    Maybe I don't even have to generate them if they are already on that one website with all the 
    number series? I'll keep thinking about how to do it elegantly though.
This is about finding an additive decomposition of an integer
Some googling suggests that a related concept in number theory is "partitions"
This isn't quite as simple as finding the partitions of a number because repeats
are not allowed. 
(added: https://en.wikipedia.org/wiki/Composition_(combinatorics) suggests that what we are after 
are "distinct paartitions")
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
(UPDATE i missed a bunch, need to isolate the missed process)
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
 then we can make the solutions for 11 from them by
- adding 1 to the first number in all of them
10,1
9,2
8,3
 8,2,1
8,4
 8,3,1
and them running the same expansion - no, that's precisely what we don't want to do
start again
adding 1 to the last number in all of them unless illegal, then the second, and so on:
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

10,1

"""