t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    m = min(s)
    sum = m * n
    indt = m
    i = s.index(m)
    while i != 0:
        m1 = min(s[:i])
        sum += (m1-indt) * (i)
        indt = m1
        i = s.index(m1)
    print(sum)
