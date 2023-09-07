# so I need to detect when I reach a value I've already reached, and that's the cycle

def to_base(number, base):
    result = ""
    while number:
        result += str(number % base)
        number //= base
    return result or ""

def minion_step(n, k, b):
    l_n = list(n)
    l_y = sorted(l_n)
    l_x = l_y[::-1]
    d_x = int(''.join(l_x), b)
    d_y = int(''.join(l_y), b)
    d_z = d_x - d_y
    z = to_base(d_z, b) # z is a atring
    pad = "0" * (k - len(z))
    z = pad + z
    #z = ''.join(l_z)
    print(n)
    print(d_x)
    print(d_y)
    print(d_z)
    print(z)
    print(len(z))
    print(pad)
    #print(z)

def minion_gen(n, k, b):
    l_n = list(n)
    while True:
        l_y = sorted(l_n)
        l_x = l_y[::-1]
        d_x = int(''.join(l_x), b)
        d_y = int(''.join(l_y), b)
        d_z = d_x - d_y
        z = to_base(d_z, b) # z is a atring
        pad = "0" * (k - len(z))
        z = pad + z
        yield z
        l_n = list(z)


#minion_step('1211',4,10)
#minion_step('210022',6,3)
#minion_step('210111',6,3)
#g = minion_gen('210111',6,3)
#for i in range(0,4):
#    print(next(g))

def solution(n, b):
    # remember n is a string!
    k = len(n)
    output = {}
    for i, id in enumerate(minion_gen(n,k,b)):
        if id in output:
            j = output[id]
            return i - j
        output[id] = i

print(solution('210022', 3))
print(solution('1211', 10))
