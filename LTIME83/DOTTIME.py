mod = 998244353


def F(a, m, p, q):
    s = 0
    for i in range(m):
        s += a[i + p - 1]*a[i + q - 1]
    return s


t = int(input())
for _ in range(t):
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        pos, val = map(int, input().split())
        a[pos-1] = val
        sum = 0
        for i in range(1, n-m+2):
            for j in range(1,n-m+2):
                sum += F(a, m, i, j) % mod
    print(sum % mod)
