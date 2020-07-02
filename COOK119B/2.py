t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    c = 0
    if m == 1:
        if a[0] == 1:
            print(-1)
        else:
            print(n)
    else:
        if a[0] > 1 or a[-1] < m-1:
            c = 0
        else:
            i = 1
            c = 1
            while i < n and a[i] < m:
                if abs(a[i] - a[i-1]) > 1:
                    c = 0
                    break
                else:
                    i += 1
                    c += 1
            while i < n and a[i] == m:
                i += 1
            while i < n and a[i] > m:
                c += (n - i)
                break
        if c == 0:
            print(-1)
        else:
            print(c)
