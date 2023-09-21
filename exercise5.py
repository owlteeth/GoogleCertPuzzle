"""
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
    yes, because (4,7) is possible - why?
    4,7
    4,3
    1,3
    1,2
    1,1
    that means that (4,11) and (11,7) are both also posible
    we also want to always be subtracting the smaller number from the bigger number
        and that means that we must never get to numbers identical (except 1,1) or one double the other (except 2,1)
        that is, if either mod is 0 it's impossible
        in fact is it impossible if both numbers are even? I think so
    there's some pattern here 
"""