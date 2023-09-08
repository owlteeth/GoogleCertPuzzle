def solution(x, y):
    """
    Implements the function specced in bunny-worker-locations (third challenge on https://foobar.withgoogle.com/)
    Returns a string representation of the calculated room id.
    At y = 1, the room id is the xth triangle number.
    As y goes up, the triangle grows accordingly, as does the 'offset' along the edge of the triangle.
    I'm sure I would write that all differently if I knew any math lol
    Completed in 2 hrs, 35 mins, 47 secs
    """
    n = triangle(x + (y - 1)) - (y - 1)
    return str(n)


def triangle(n):
    return n * (n + 1) // 2
