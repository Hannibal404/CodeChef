t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    c = []
    for i in range(n):
        c.append(min(list(map(int, input().split()))))
    print(" ".join(c))


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    c = []
    for i in range(n):
        a = list(map(int, input().split()))
        x, xc = 1, a.count(1)
        if m > 1:
            for i in range(2, m+1):
                ic = a.count(i)
                if ic > 0 and ic < xc:
                    x, xc = i, ic
                elif ic > 0 and xc == 0:
                    x, xc = i, ic
        c.append(str(x))
    print(" ".join(c))
