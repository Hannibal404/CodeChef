t = int(input())
for _ in range(t):
    n, = map(int, input().split())
    a = list(map(int, input().split()))
    c = [0 for i in range(200001)]
    x = 0
    for i in a:
        c[i] += 1
        if c[i] == 3:
            print("NO")
            x = -1
            break
    if x == -1:
        continue
    if c[max(a)] > 1:
        print("NO")
        continue
    else:
        print("YES")
        x = []
        m = len(c)
        for i in range(m):
            if c[i] > 0:
                c[i] -= 1
                x.append(i)
        for i in range(m):
            if c[m-i-1] == 1:
                x.append(m-i-1)
        print(*x)
