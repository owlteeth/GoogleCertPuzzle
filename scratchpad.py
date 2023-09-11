import sys 

sys.setrecursionlimit(3500)
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


def solution(n):
    n = int(n)
    steps = solution_recursive(n)
    return steps


print(solution(4))
print(solution(15))
print(solution(10**309))
