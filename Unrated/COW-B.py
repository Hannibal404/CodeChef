t = int(input())
for _ in range(t):
    n, = map(int, input().split())
    a = list(map(int, input().split()))
    m, = map(int, input().split())
    b = list(map(int, input().split()))
    dc = {}
    for i in b:
        if i in dc.keys():
            dc[i] += 1
        else:
            dc[i] = 1
    c = 0
    dkey = set(dc.keys())
    for i in range(1,n):
        if a[i] not in dkey:
            if a[i-1] in dkey:
                c += 1
    if a[n-1] in dkey:
        c += 1
    print(c)