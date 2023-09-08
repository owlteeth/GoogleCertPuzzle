def to_base(number, base):
    """Returns a string containing the integer mapped to a base. Only works up to base 10
    but that's known good for this scenario.
    Completed in 4 hrs, 8 mins, 36 secs (actually less as I stopped for dinner before submitting).
    """
    result = ""
    while number:
        result += str(number % base)
        number //= base
    return result


def minion_gen(first_id, base):
    """Generates an arbitrary number of minion IDs per the provided algo;
    they will start looping after a certain point."""
    size = len(first_id)
    next_id = first_id
    while True:
        list_y = sorted(list(next_id))
        list_x = list_y[::-1]
        x = int("".join(list_x), base)
        y = int("".join(list_y), base)
        z = x - y
        next_id = to_base(z, base)
        padding = "0" * (size - len(next_id))
        next_id = padding + next_id
        yield next_id


def solution(n, b):
    """Implements the function specced in hey-i-already-did-that (second challenge on https://foobar.withgoogle.com/)
    Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n.
    """
    # collect generated IDs with their generation number in a dict
    output = {}
    for i, id in enumerate(minion_gen(n, b)):
        past_i = output.get(id, None)
        if past_i:
            return i - past_i
        output[id] = i


assert solution("1211", 10) == 1
assert solution("210022", 3) == 3
