t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d1, d2, d3 = b[0]-a[0], b[1]-a[1], b[2]-a[2]
    r1, r2, r3 = b[0]-a[0], b[1]-a[1], b[2]-a[2]
    if b == a:
        print(0)
    elif d1 == d2 and d1 == d3:
        print(1)
    elif r1 == r2 and r1 == r3 and int(r1) == r1:
        print(1)
