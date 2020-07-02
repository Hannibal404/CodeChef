t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    aset = set(a)
    cm = a.count(m)
    x = 0
    for i in range(1, m):
        if i in aset:
            continue
        else:
            x = -1
            break
    if x == -1:
        print(-1)
        continue
    else:
        print(n - cm)
