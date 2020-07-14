t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    m = a[-1]
    if x >= m:
        print(n)
        continue
    d, i, cure = 0, 0, 0
    while i < n and a[i] < x//2:
        i += 1
    while i < n:
        while i < (n - 1) and a[i] < x//2:
            i += 1
        while x < a[i]:
            x *= 2
            d += 1
        cure += 1
        x = 2 * a[i]
        d += 1
        i += 1
    d += n - cure
    print(d)
