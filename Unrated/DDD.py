def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a*b) / gcd(a, b)


n, = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
ml = 1
for i in range(n-1):
    for j in range(i+1, n):
        if a[i]*a[j] <= ml:
            break
        lc = lcm(a[i], a[j])
        if lc > ml:
            ml = lc
print(int(ml))
