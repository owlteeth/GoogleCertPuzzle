
def to_base(number, base):
    base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    return int(result[::-1]) or 0


def to_base_simpler(number, base):
    #base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while number:
        result.append(number % base)
        number //= base
    result.reverse()
    return result or []

x = to_base_simpler(123,3)
print(x)
print(type(x))
"""
0 -> 0
2 -> 2

"""