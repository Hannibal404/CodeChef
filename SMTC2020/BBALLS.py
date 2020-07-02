from math import log2

t = int(input())
for _ in range(t):
    m = int(input())
    b = 0
    while m > 1:
        x = int(log2(m))
        if x == log2(m):
            break
        m -= 2**(x)
        b += 1
    print(b)
