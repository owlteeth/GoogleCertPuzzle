# division problem
# three operations increment, decrement, divide by 2 if even
# find shortest sequence to reduce n<= 309 (why?) to 1
# something about getting it to a power of 2
# 

POWERS_OF_2 = {1,2,4,8,16,32,64,128,256}
solution = []

def record(item):
    #global solution
    #solution.append(item)
    pass

def solution_recursive(n, spread, steps):
    if n <= 1: # base case
        return steps
        #return steps
    # if n is even, can't do better than immediately /2
    if not n % 2:
        n = int(n/2)
        steps += 1
        record(n)
        return solution_recursive(n, spread, steps)
    else: #n is odd
        #look for a close power of 2 (more elegant way with sets?)
        for i in range(spread,0,-1):
            if (n-i in POWERS_OF_2):
                o = n
                p = ">" * i
                n -= i
                steps += i
                record(f"{o}{p}{n}")
                return solution_recursive(n, spread, steps)
            elif (n+i in POWERS_OF_2):
                o = n
                p = ">" * i
                n += i
                steps += i
                record(f"{o}{p}{n}")
                return solution_recursive(n, spread, steps)
        # search failed
        n -= 1
        steps += 1
        record(n)
        return solution_recursive(n, spread, steps)
    
def solution(n):
    n = int(n)
    steps = solution_recursive(n, 1, 0)
    print(f"{n} -> {solution} len {steps}")
    return steps


def tester():
    ns = range(1, 310)
    spreads = range(0, 11)
    results = []
    for spread in spreads:
        line = [solution_recursive(n, spread, 0) for n in ns]
        print(f"total steps using spread {spread}: {sum(line)}")


"""

def solution_iterative(n):
    spread = 5
    steps = 0
    while n>1:
        #checklist = {p-n for x in POWERS_OF_2}
        #distance = min(checklist)
        # if n is even, can't do better than immediately  /2
        if not n % 2:
            n = n/2
            steps += 1
        elif: #n is odd
            for i in range(spread):
                if (n-i in POWERS_OF_2):
                    n -= i
                    steps += i
                elif (n+i in POWERS_OF_2):
                    n += i
                    steps += i
        else
            if n % 2: # n is odd
                if (n+1 in POWERS_OF_2):
                    n += 1


    return steps
"""

solution(4)
solution(15)  
solution(301)  
#tester()

"""
If I use -1 at point a, tests  1,2,4 and 9 pass
If I use +1 instead, test 8 passes and 4 fails!
"""