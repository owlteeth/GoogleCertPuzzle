
def solution(s):
    """Implements the function specced in the-cake-is-not-a-lie (first challenge on https://foobar.withgoogle.com/)
    Given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.
    """
    cake = s
    mnms = len(cake)
    # find all whole divisors of mnms
    # naive but cake is bounded <200 so it should be efficient enough 
    candidates = range(1, mnms + 1)
    divisors = [n for n in candidates if not mnms % n]
     # we want to test largest divisors first
    divisors.reverse()
    
    for divisor in divisors:
        slice = mnms // divisor
        cuttings = [cake[mark : mark + slice] for mark in range(0, mnms, slice)]
        patterns = set(cuttings)
        #print(f"cake into {divisor} is: {cuttings}, {len(patterns)} unique")
        
        if len(patterns) == 1: # don't need another case since all cakes divisible by 1
            return divisor
