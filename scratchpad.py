def rsum(n):
    return n*(n+1)/2

def thingy(x,y):
    return rsum(x) + rsum(x+y) #if this is it, must be a way to reuse the work in first part

a = rsum(5)
b = rsum(4)
print(a)
print(b)