import math


def primeFactors(n):
    c = 0

    while n % 2 == 0:
        c += 1
        n = n // 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            c += 1
            n = n // i
    if n > 2:
        c += 1
    return c


t = int(input())
for i in range(t):
    x, k = map(int, input().split())  # x=no.of div, k=prime divisors
    z = primeFactors(x)
    if z >= k:
        print(1)
    else:
        print(0)
