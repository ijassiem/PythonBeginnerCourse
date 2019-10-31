def fact(n):
    out = 1
    for i in range(1, n+1):
        out*= i
    return out

def factr(n):
    if n<=1:
        return 1
    else:
        return n * factr(n-1)

print(fact(4))

print(factr(4))
