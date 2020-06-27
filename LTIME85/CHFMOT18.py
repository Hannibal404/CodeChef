t = int(input())
for _ in range(t):
    s, n = map(int, input().split())
    if s <= n:
        if s == 1:
            print(1)
        elif s % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        c = s//n
        s = s % n
        if s == 0:
            pass
        elif s == 1:
            c += 1
        elif s % 2 == 0:
            c += 1
        else:
            c += 2
        print(c)
