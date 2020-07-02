t = int(input())
for _ in range(t):
    ts = int(input())
    if ts % 2 != 0:
        print(ts//2)
    else:
        c = 1
        x = ts
        while x % 2 == 0:
            c += 1
            x //= 2
        j = 2**c
        print(ts//j)
